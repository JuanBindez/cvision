from ultralytics import YOLO


class Vision():
    def __init__(self, video_mp4):
        self.video_mp4 = video_mp4

    def persons_counter(self):
        model = YOLO('yolov8n.pt')
        video_path = self.video_mp4
        results = model(video_path, save=True, save_txt=True)

        total_person_count = 0
        
        for frame_results in results:
            person_detections = [det for det in frame_results.boxes if det.cls == 0]
            person_count = len(person_detections)
            total_person_count += person_count

        return total_person_count

    def detect_persons(self):
        model = YOLO('yolov8n.pt')
        results = model(source=self.video_mp4, show=True, conf=0.4, save=True)

class RealTime():
    def run(self):
        model = YOLO('yolov8n.pt')
        results = model(source=0, show=True, conf=0.4, save=True)