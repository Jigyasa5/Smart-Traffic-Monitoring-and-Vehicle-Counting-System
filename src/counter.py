import cv2

class VehicleCounter:

    def __init__(self, line_y):

        self.line_y = line_y
        self.offset = 15

        self.vehicle_count = 0

        # Store already counted vehicle centers
        self.counted_centers = []

    def count_vehicle(self, cx, cy):

        if self.line_y - self.offset <= cy <= self.line_y + self.offset:

            for px, py in self.counted_centers:

                distance = ((cx - px) ** 2 + (cy - py) ** 2) ** 0.5

                if distance < 50:
                    return

            self.vehicle_count += 1
            self.counted_centers.append((cx, cy))

            # Prevent list from growing forever
            if len(self.counted_centers) > 500:
                self.counted_centers.pop(0)

    def draw_line(self, frame, width):

        cv2.line(
            frame,
            (0, self.line_y),
            (width, self.line_y),
            (255, 0, 0),
            3
        )