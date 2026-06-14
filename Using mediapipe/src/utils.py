import cv2


VEHICLE_CLASSES = [
    "car",
    "truck",
    "bus",
    "motorcycle",
    "bicycle"
]


def draw_box(frame, x, y, w, h, label, score):

    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"{label} {score:.2f}",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )


def draw_center(frame, cx, cy):

    cv2.circle(
        frame,
        (cx, cy),
        4,
        (255, 0, 0),
        -1
    )