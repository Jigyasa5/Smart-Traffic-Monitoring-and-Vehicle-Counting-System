import json
import os


def save_report(
    total_frames,
    total_detected,
    vehicle_count,
    processing_time
):

    report = {
        "video_name": "traffic.mp4",
        "total_frames": total_frames,
        "total_vehicles_detected": total_detected,
        "total_vehicles_counted": vehicle_count,
        "processing_time_seconds": processing_time
    }

    os.makedirs("output", exist_ok=True)

    with open("output/report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("Report saved successfully!")