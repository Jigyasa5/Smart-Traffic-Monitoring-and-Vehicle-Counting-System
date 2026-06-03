import cv2
import time
import os

from detector import VehicleDetector
from counter import VehicleCounter
from utils import save_report

os.makedirs("output", exist_ok=True)

# Input video path
video_path = "Input/traffic.mp4"

cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Cannot open video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0 or fps is None:
    fps = 25

# Get video frame width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(
    "Output/processed_video.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

detector = VehicleDetector()

# Define counting line position 
line_y = int(height * 0.65)

counter = VehicleCounter(line_y)

total_detected = 0

start_time = time.time()

# Process video frame by frame
while True:

    ret, frame = cap.read()

    if not ret:
        break

    boxes = detector.detect(frame)

    total_detected += len(boxes)

    for (x, y, w, h) in boxes:
        # Draw green bounding box around vehicle
        pad = 10

        x1 = max(0, x - pad)
        y1 = max(0, y - pad)

        x2 = min(width, x + w + pad)
        y2 = min(height, y + h + pad)
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Calculate center point of bounding box
        cx = x + w // 2
        cy = y + h 

        cv2.circle(
            frame,
            (cx, cy),
            4,
            (0, 0, 255),
            -1
        )

        counter.count_vehicle(cx, cy)

    # Draw counting line on frame
    counter.draw_line(frame, width)

    cv2.putText(
        frame,
        f"Vehicle Count: {counter.vehicle_count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    out.write(frame)

    cv2.imshow("Traffic Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

processing_time = time.time() - start_time

report = save_report(
    "traffic.mp4",
    total_detected,
    counter.vehicle_count,
    processing_time
)

print(report)

cap.release()
out.release()
cv2.destroyAllWindows()