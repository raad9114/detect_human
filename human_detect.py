import mediapipe as mediapipe  #pip install mediapipe
import cv2 #pip install opencv-python

#declare variables
readVideo = cv2.VideoCapture(0) #video capture variable
mediapipePose = mediapipe.solutions.pose #mediapipe pose variable
poseDetect = mediapipePose.Pose() #mediapipe pose variable
mediapipeDrawingUtils = mediapipe.solutions.drawing_utils #mediapipe draw variable

#make the conditions 
while True:
    show,img = readVideo.read()
    # if not show:
    #     break
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = poseDetect.process(imgRGB)

    mediapipeDrawingUtils.draw_landmarks(img,results.pose_landmarks,mediapipePose.POSE_CONNECTIONS)

    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break