# Smart Traffic Monitoring and Vehicle Counting System

A Computer Vision project developed using **Python**, **OpenCV**, and **NumPy** to detect, track, and count vehicles from traffic videos. The system analyzes video frames, identifies moving vehicles, draws bounding boxes, counts vehicles crossing a virtual line, and generates useful traffic statistics.

---

## Features

* Vehicle Detection using Background Subtraction (MOG2)
* Vehicle Tracking using Contour Detection
* Bounding Box Visualization
* Vehicle Counting with Virtual Counting Line
* Traffic Statistics Generation
* Processed Video Output Saving
* Real-Time Video Display

---

## Technologies Used

* Python
* OpenCV
* NumPy

---

## Project Structure

```text
Smart-Traffic-Monitoring-and-Vehicle-Counting-System/
│
├── Input/
│   └── traffic.mp4
│
├── Output/
│   └── processed_video.mp4
|   └── report.json
│
├── src/
│   ├── main.py
│   ├── detector.py
│   ├── counter.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Jigyasa5/Smart-Traffic-Monitoring-and-Vehicle-Counting-System.git
cd Smart-Traffic-Monitoring-and-Vehicle-Counting-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

Place your traffic video inside the **Input** folder and run:

```bash
python src/main.py
```

Press **Q** to quit the application.

---

## 🔍 Working Flow

1. Read traffic video frame by frame.
2. Apply Background Subtraction (MOG2).
3. Perform Morphological Operations to remove noise.
4. Detect moving vehicles using contours.
5. Draw bounding boxes around detected vehicles.
6. Track vehicle centers.
7. Count vehicles crossing the counting line.
8. Save processed video and generate statistics.

---

## Output

The system provides:

* Detected Vehicle Bounding Boxes
* Vehicle Count Display
* Processed Output Video

---

## Author

**Jigyasa**

---

## License

This project is created for educational and learning purposes.
