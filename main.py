import cv2
from tracker import *
import os
import vlc

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def main():
    # Create tracker object
    tracker = EuclideanDistTracker()
    # https://cwwp2.dot.ca.gov/vm/streamlist.htm
    cap = cv2.VideoCapture("rtsp://192.168.1.213:554/11")


    # Object detection from Stable camera
    object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40, detectShadows=True)
    while True: # while(cap.isOpened()):
        ret, frame = cap.read()
        frame = rescale_frame(frame, percent=45)
        height, width, _ = frame.shape
        print (height, width, _)

        # Extract Region of interest
        #  roi = frame[340: 720,500: 800]

        # Extract Region of interest
        # roi = frame[200: 400,0: 220]

        # Extract Region of interest
        roi = frame[0: 864,0: 1152]
    

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
                cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 2)
                x, y, w, h = cv2.boundingRect(cnt)


                detections.append([x, y, w, h])

        # 2. Object Tracking
        boxes_ids = tracker.update(detections)
        for box_id in boxes_ids:
            x, y, w, h, id = box_id
            cv2.putText(roi, "obj: " + str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.imshow("roi", roi)
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)

        key = cv2.waitKey(30)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


main()
