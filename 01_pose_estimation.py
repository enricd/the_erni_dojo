import cv2 as cv
import mediapipe as mp
from time import time


class poseDetector():

    def __init__(self, 
                static_image_mode=False,
                model_complexity=1,
                smooth_landmarks=True,
                enable_segmentation=False,
                smooth_segmentation=True,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5):

        self.static_image_mode = static_image_mode
        self.model_complexity = model_complexity
        self.smooth_landmarks = smooth_landmarks
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.static_image_mode,
                                    self.model_complexity,
                                    self.smooth_landmarks,
                                    self.enable_segmentation,
                                    self.smooth_segmentation,
                                    self.min_detection_confidence,
                                    self.min_tracking_confidence)


    def findPose(self, img, draw=True):
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        #print(results.pose_landmarks)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    
    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id, lm)
                cx, cy = int(lm.x*w), int(lm.y*h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 10, (255, 0, 0), cv.FILLED)
        
        return self.lmList


def main(is_video=True):

    if is_video:
        fourcc = cv.VideoWriter_fourcc(*'MJPG')
        #out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 1500))
        detector = poseDetector()
        #cap = cv.VideoCapture('Reza Alipour 5.63 seconds short.mp4')
        cap = cv.VideoCapture(0)

    else:
        detector = poseDetector(static_image_mode=True, model_complexity=2, min_detection_confidence=0.2)
        img = cv.imread('photos/speedclimbing/Screenshot from 2022-02-10 22-57-47.png')

    pTime = 0

    if is_video:
        i = 0
        while True:
            i += 1
            success, img = cap.read()
            img = detector.findPose(img)
            lmList = detector.findPosition(img, draw=False)
            #print(lmList)
            if len(lmList) > 14:
                cv.circle(img, (lmList[24][1], lmList[24][2]), 10, (255, 0, 0), cv.FILLED)
            
            cTime = time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            cv.putText(img, str(i) + '   ' + str(int(fps)), (70, 50), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
            cv.imshow('Image', img)

            #out.write(img)

            cv.waitKey(1)
    
    else:
        detector.findPose(img)
        cv.imshow('Image', img)

        cv.waitKey(0)


    if is_video:
        #out.realease()
        cap.release()


if __name__ == '__main__':
    main(is_video=True)
    cv.destroyAllWindows()