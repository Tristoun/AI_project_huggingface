import cv2
from ultralytics import YOLO
import numpy as np
import supervision as sv
import logging

logging.getLogger("ultralytics").setLevel(logging.ERROR)

class ObjectDetection() :
    def __init__(self, camera = 0, model_path = "yolov8n.pt") :
        self.cap = cv2.VideoCapture(camera)
        self.model = YOLO(model_path, verbose=False)


    def process_frame(self, frame):
        result = self.model(frame)[0]
        detections = sv.Detections.from_ultralytics(result)

        box_annotator = sv.BoxAnnotator()
        label_annotator = sv.LabelAnnotator()

        labels = [
            f"{class_name} {confidence:.2f}"
            for class_name, confidence
            in zip(detections['class_name'], detections.confidence)
        ]

        annotated_frame = box_annotator.annotate(scene=frame, detections=detections)
        annotated_frame = label_annotator.annotate(scene=annotated_frame, detections=detections, labels=labels)
        return annotated_frame

    def detect_object(self):

        while True:
            ret, frame = self.cap.read()

            if not ret:
                print("Failed to capture frame")
                break

            annotated_frame = self.process_frame(frame)

            cv2.imshow("yolov8", annotated_frame)

            if (cv2.waitKey(20) & 0xFF) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    Objdetect = ObjectDetection()
    Objdetect.detect_object()