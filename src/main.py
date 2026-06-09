import cv2
import time
import os

from detector import VehicleDetector
from counter import VehicleCounter
from utils import save_report


cap = cv2.VideoCapture("Input/traffic.mp4")

os.makedirs("output", exist_ok=True)



# Video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print("FPS:", fps)
print("Width:", width)
print("Height:", height)
print("Total Frames:", total_frames)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(
    "output/output_video.mp4",
    fourcc,
    fps,
    (800, 600)
)
detector = VehicleDetector()
counter = VehicleCounter()

start_time = time.time()

# Frame Extraction
while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))

    contours = detector.detect(frame)

    # Draw Counting Line
    cv2.line(frame, (120, 460),(620, 420),(0, 0, 255),3)

    frame = counter.process_contours(
        frame,
        contours
    )

    cv2.putText(
        frame,
        f"Vehicle Count: {counter.vehicle_count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.imshow("Traffic Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()

processing_time = round(
    time.time() - start_time,
    2
)

print("Total Vehicles Counted:",
      counter.vehicle_count)


save_report(
    total_frames,
    counter.total_detected,
    counter.vehicle_count,
    processing_time
)