import cv2
import numpy as np
import face_recognition
import os
import csv
from datetime import datetime

# Load known faces
known_face_encodings = []
known_face_names = []

print("🧠 Loading known faces...")
path = "ImagesAttendance"
for filename in os.listdir("students"):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        img = face_recognition.load_image_file(f"{"students"}/{filename}")
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            known_face_encodings.append(encodings[0])
            known_face_names.append(os.path.splitext(filename)[0])
        else:
            print(f"⚠️ No face encoding found in {filename}, skipping.")

students = known_face_names.copy()
f = open("Attandence.csv",'w+',newline='')
lnwriter = csv.writer(f)

# Attendance file setup
def mark_attendance(name):

        all_data = f.readlines()
        names = [line.split(',')[0] for line in all_data]
        if name not in names:
            now = datetime.now()
            if name in students:
                f.write(f"{" "+ name}, {" "+ now.strftime('%H:%M:%S')}, {" "+ now.strftime('%Y-%m-%d')}\n")
                students.remove(name)
                print(f"✅ Marked attendance for: {name}")

# Start camera
print("📸 Starting camera... Press 'q' to quit.")
video = cv2.VideoCapture(0)

while True:
    success, frame = video.read()
    if not success:
        print("❌ Failed to capture frame.")
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                mark_attendance(name)

        # Show results on frame
        top, right, bottom, left = [v * 4 for v in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 200), 2)
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 200), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    cv2.QT_FONT_NORMAL, 0.6, (0, 0, 0),1)

    cv2.imshow('Attendance System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()