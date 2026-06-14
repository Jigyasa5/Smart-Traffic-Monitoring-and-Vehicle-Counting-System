import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class VehicleDetector:

    def __init__(self, model_path):

        base_options = python.BaseOptions(
            model_asset_path=model_path
        )

        options = vision.ObjectDetectorOptions(
            base_options=base_options,
            score_threshold=0.5,
            max_results=10
        )

        self.detector = vision.ObjectDetector.create_from_options(
            options
        )

    def detect(self, frame):

        rgb = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=frame
        )

        result = self.detector.detect(rgb)

        return result.detections