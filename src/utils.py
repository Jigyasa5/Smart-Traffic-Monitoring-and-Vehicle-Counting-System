import json

def save_report(
    video_name,
    total_detected,
    total_counted,
    processing_time
):

    report = {
        "video_name": video_name,
        "total_vehicles_detected": total_detected,
        "total_vehicles_counted": total_counted,
        "processing_time_seconds": round(processing_time, 2)
    }

    with open("output/report.json", "w") as f:
        json.dump(report, f, indent=4)

    return report