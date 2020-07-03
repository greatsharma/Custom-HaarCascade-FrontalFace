import cv2
import time
import numpy as np


facedetector_default = cv2.CascadeClassifier("models/default.xml")
facedetector_custom1 = cv2.CascadeClassifier("models/custom1.xml")
facedetector_custom2 = cv2.CascadeClassifier("models/custom2.xml")
facedetector_custom3 = cv2.CascadeClassifier("models/custom3.xml")


def draw_text_with_backgroud(img, text, x, y, font_scale, thickness=1, font=cv2.FONT_HERSHEY_SIMPLEX,
                            background=(0,0,0), foreground=(255,255,255), box_coords_1=(-5,5), box_coords_2=(5,-5)):
    (text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]
    box_coords = ((x+box_coords_1[0], y+box_coords_1[1]), (x + text_width + box_coords_2[0], y - text_height + box_coords_2[1]))
    cv2.rectangle(img, box_coords[0], box_coords[1], background, cv2.FILLED)
    cv2.putText(img, text, (x, y), font, fontScale=font_scale, color=foreground, thickness=thickness)


def detect_face(facedetector, frame, gray_frame, scaleFactor, minNeighbors, minSize=(30,30)):
    tik = time.time()
    faces = facedetector.detectMultiScale(gray_frame, scaleFactor, minNeighbors, minSize=minSize)
    tt = time.time() - tik
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0), 3)
    return tt


tt_default = 0
tt_custom1 = 0
tt_custom2 = 0
tt_custom3 = 0
frame_count = 0

cv2.namedWindow("haar cascades comparison", cv2.WINDOW_NORMAL)
cv2.resizeWindow("haar cascades comparison", 1400, 700)

vidcap = cv2.VideoCapture(0)
while True:
    status, frame1 = vidcap.read()
    if not status:
        break

    frame_count += 1

    frame1 = cv2.flip(frame1, 1, 0)
    frame2 = frame1.copy()
    frame3 = frame1.copy()
    frame4 = frame1.copy()

    gray_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    tt_default += detect_face(facedetector_default, frame1, gray_frame, 1.3, 5)
    text = f"default, fps: {round(frame_count/tt_default, 2)}"
    draw_text_with_backgroud(frame1, text, 25, 25, font_scale=0.6, thickness=2)

    tt_custom1 += detect_face(facedetector_custom1, frame2, gray_frame, 1.025, 4)
    text = f"custom1, fps: {round(frame_count/tt_custom1, 2)}"
    draw_text_with_backgroud(frame2, text, 25, 25, font_scale=0.7, thickness=2)

    tt_custom2 += detect_face(facedetector_custom2, frame3, gray_frame, 1.1, 5)
    text = f"custom2, fps: {round(frame_count/tt_custom2, 2)}"
    draw_text_with_backgroud(frame3, text, 25, 25, font_scale=0.7, thickness=2)

    tt_custom3 += detect_face(facedetector_custom3, frame4, gray_frame, 1.2, 4)
    text = f"custom3, fps: {round(frame_count/tt_custom3, 2)}"
    draw_text_with_backgroud(frame4, text, 25, 25, font_scale=0.7, thickness=2)

    top = np.hstack((frame1, frame2))
    bottom = np.hstack((frame3, frame4))
    final_frame = np.vstack((top, bottom))
    cv2.imshow("haar cascades comparison", final_frame)
    if cv2.waitKey(10) == ord('q'):
        break

vidcap.release()
cv2.destroyAllWindows()