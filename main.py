import cv2
from tracker import *
import time
import os

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def main():
    # clear tracked objects from previous run
    if(os.path.exists("objects.csv")):
        os.remove("objects.csv")


    # Create tracker object
    tracker = EuclideanDistTracker()
    # https://cwwp2.dot.ca.gov/vm/streamlist.htm
    cap = cv2.VideoCapture("rtsp://192.168.1.213:554/11")


    # Object detection from Stable camera
    object_detector = cv2.createBackgroundSubtractorKNN(history=50000, dist2Threshold=90, detectShadows=False)
    while True:
        ret, frame = cap.read()
        frame = rescale_frame(frame, percent=45)
        height, width, _ = frame.shape

        # Extract Region of interest
        roi = frame[300: 420,0: 1152]
    

        # 1. Object Detection
        mask = object_detector.apply(roi)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        detections = []
        for cnt in contours:
            # Calculate area and remove small elements
            area = cv2.contourArea(cnt)
            if area > 400:
                # Draw contours if needed
                cv2.drawContours(roi, [cnt], -1, (0, 0, 255), )
                x, y, w, h = cv2.boundingRect(cnt)
                detections.append([x, y, w, h])

        # 2. Object Tracking
        boxes_ids = tracker.update(detections)
        for box_id in boxes_ids:
            x, y, w, h, id = box_id
            cv2.putText(roi, "obj: " + str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.putText(frame, 'Detection Region', (50, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)    
        cv2.rectangle(frame, (0,300), (1152,420), (0, 255, 0), 1)
        cv2.imshow("Masked Region", mask)
        cv2.imshow("Detection Region", roi)
        # cv2.imshow("Frame", frame)

        key = cv2.waitKey(30)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
