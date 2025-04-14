# 🎓 Automatic Attendance System with Face Recognition

> This project is a Python-based attendance system that uses real-time face recognition to automatically mark student attendance. <br> Built with `face_recognition`, `OpenCV`, and `dlib`, it streamlines the attendance process with AI-powered face matching.

## 📸 Features

- Real-time face recognition using webcam
- Auto attendance logging to a `.csv` file
- Detects multiple faces and avoids duplicates
- Easy-to-train with your own student images

## 🧠 Tech Stack

- Python 3.x
- OpenCV
- face_recognition (built on dlib)
- NumPy
- CSV file handling

## 📁 Directory Structure 

```dart
Automatic-Attendance-System/
├── images/                 # Folder with known student images
│   ├── student1.jpg
│   ├── student2.jpg
├── attendance.csv          # Output attendance file
├── main.py                 # Main script
├── README.md               # This file
├── requirements.txt        # Dependencies

```
#

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Vishal2186/Automatic-Attendance-System.git
cd Automatic-Attendance-System
```
### 2. Create a virtual environment (recommended)

```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add student images
 - Place clear, front-facing photos of students in the images/ folder.
 - The image filename (without extension) will be used as the student name.

### 5. Run the program

```bash
python main.py
```
  Press q to quit the webcam view.
  <br><br>




<table>
    <tbody border="0" cellspacing="0" cellpadding="0">
        <tr  style="width:70%">
           <td rowspan=6>


## ✅ Output
 - Attendance is saved to attendance.csv with the student’s name and timestamp.
 - Duplicate entries are prevented — attendance is only marked once per student per session.

## 🛠️ Notes
 - Make sure lighting is good for accurate face detection.
 - If no face encodings are found, check image clarity and angle.
 - The first-time model load may take a few seconds.
   
    </td>
        </tr>
           <tr>
            <td><img src="https://pyimagesearch.com/wp-content/uploads/2018/06/face_recognition_opencv_example_02.jpg"alt="view" align="right" />
           </td>
        </tr>      
   </tbody>
</table>
