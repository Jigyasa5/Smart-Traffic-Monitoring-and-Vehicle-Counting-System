import cv2
import mediapipe as mp

from detector import VehicleDetector
from counter import VehicleCounter
from utils import *

# ==================================
# Initialization
# ==================================

detector = VehicleDetector(
    "model/efficientdet_lite0.tflite"
)

counter = VehicleCounter(
    line_y=450,
    offset=15
)

cap = cv2.VideoCapture(
    "Input/traffic.mp4"
)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = 800
height = 600

# Create VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(
    "output.mp4",
    fourcc,
    fps,
    (width, height)
)

# ==================================
# Video Writer
# ==================================

width = 800
height = 600
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(
    "Output/output.mp4",
    fourcc,
    fps,
    (width, height)
)

# ==================================
# Processing
# ==================================

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(
        frame,
        (width, height)
    )

    cv2.line(
        frame,
        (180, counter.line_y),
        (600, counter.line_y),
        (0, 0, 255),
        3
    )

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    detections = detector.detect(
        rgb_frame
    )

    for detection in detections:

        category = detection.categories[0]

        label = category.category_name.lower()
        score = category.score

        if label not in VEHICLE_CLASSES:
            continue

        bbox = detection.bounding_box

        x = int(bbox.origin_x)
        y = int(bbox.origin_y)
        w = int(bbox.width)
        h = int(bbox.height)

        if w * h < 1500:
            continue

        draw_box(
            frame,
            x, y, w, h,
            label,
            score
        )

        cx = x + w // 2
        cy = y + h // 2

        draw_center(
            frame,
            cx,
            cy
        )

        counted = counter.update(
            cx,
            cy
        )

        if counted:

            cv2.line(
                frame,
                (0, counter.line_y),
                (800, counter.line_y),
                (0, 255, 0),
                3
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

    # Save frame to output video
    out.write(frame)

    cv2.imshow(
        "Vehicle counting",
        frame
    )

    out = cv2.VideoWriter(
    "Output/output.mp4",
    fourcc,
    fps,
    (width, height)
)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ==================================
# Cleanup
# ==================================

cap.release()
out.release()

cv2.destroyAllWindows()

print(
    "Total Vehicles Counted:",
    counter.vehicle_count
)