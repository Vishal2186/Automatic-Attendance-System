from PIL import Image
import cv2
import face_recognition

# Registor a student directly
def RegistorNewStudent():
    index = 0
    names = []
    while True:
        student_name = input("Enter student {} name = ".format(index))
        if student_name == "exit":
            break
        names.insert(index,student_name)
        index += 1
    

    for name in names:
        while True:
            video = cv2.VideoCapture(0)
            succes ,frame = video.read()
            cv2.imshow("Registration",frame)
            if not succes:
                print("Failed to grab frame")
                break

            k = cv2.waitKey(1)
            if k%256 == 27:
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                img_name = name + ".jpg"
                cv2.imwrite("students/" + img_name,frame)
                print("✅ {} Written!".format(img_name))
                break
            
    video.release()
    cv2.destroyAllWindows()
RegistorNewStudent()