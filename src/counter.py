import cv2


class VehicleCounter:

    def __init__(self):

        self.vehicle_count = 0
        self.total_detected = 0
        self.false_positive_count = 0

        self.line_y = 300
        self.offset = 10

        self.detected_centers = []

    def process_contours(self, frame, contours):

        for contour in contours:

            area = cv2.contourArea(contour)

            if area < 1500:
                self.false_positive_count += 1
                continue

            x, y, w, h = cv2.boundingRect(contour)

            aspect_ratio = w / h

            if aspect_ratio < 0.6 or aspect_ratio > 3.5:
                self.false_positive_count += 1
                continue

            box_area = w * h
            fill_ratio = area / box_area

            if fill_ratio < 0.4:
                self.false_positive_count += 1
                continue

            self.total_detected += 1

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cx = x + w // 2
            cy = y + h // 2

            cv2.circle(
                frame,
                (cx, cy),
                4,
                (255, 0, 0),
                -1
            )

            if abs(cy - self.line_y) < self.offset:

                if (cx, cy) not in self.detected_centers:

                    self.detected_centers.append((cx, cy))
                    self.vehicle_count += 1

        return frame