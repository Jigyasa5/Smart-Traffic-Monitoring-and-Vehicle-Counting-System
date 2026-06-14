class VehicleCounter:

    def __init__(self, line_y=300, offset=15):

        self.vehicle_count = 0
        self.line_y = line_y
        self.offset = offset
        self.counted = []

    def update(self, cx, cy):

        if self.line_y - self.offset <= cy <= self.line_y + self.offset:

            counted_before = False

            for px, py in self.counted:

                distance = (
                    (cx - px) ** 2 +
                    (cy - py) ** 2
                ) ** 0.5

                if distance < 50:
                    counted_before = True
                    break

            if not counted_before:

                self.counted.append((cx, cy))
                self.vehicle_count += 1

                return True

        return False
    