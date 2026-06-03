import cv2
import numpy as np

class VehicleDetector:

    def __init__(self):

        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(
            history=1000,
            varThreshold=30,
            detectShadows=False
        )

        self.kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (9, 9)
        )

    def detect(self, frame):

        mask = self.bg_subtractor.apply(frame)

        cv2.imshow("Mask", mask)

        _, mask = cv2.threshold(
            mask,
            200,
            255,
            cv2.THRESH_BINARY
        )

        # Remove noise
        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            self.kernel,
            iterations=2
        )

        # Join nearby vehicle parts
        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_CLOSE,
            self.kernel,
            iterations=3
        )

        # Merge fragmented contours
        mask = cv2.dilate(
            mask,
            self.kernel,
            iterations=2
        )

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        boxes = []

        for cnt in contours:

            area = cv2.contourArea(cnt)

            if area < 2500:
                continue

            x, y, w, h = cv2.boundingRect(cnt)

            if w < 40 or h < 40:
                continue

            ratio = w / float(h)

            if ratio < 0.5 or ratio > 5:
                continue

            boxes.append((x, y, w, h))

        return boxes