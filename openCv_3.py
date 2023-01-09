import numpy as np
import cv2

cap=cv2.VideoCapture(0) # Number of video devices i.e if we want to access 1st device or 1 or we can add video file too

while True:
    ret,frame=cap.read() # get frame(numpy array) and return value for that frame to check if proper
    width=int(cap.get(3))#Width of the video capture(There 17 diff properties)
    height=int(cap.get(4))#Height of the video capture(There 17 diff properties)
    image=np.zeros(frame.shape,np.uint8) #taking a dummy image

    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5) #Shrinking each image by half of the image
    image[:height//2,:width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180)#Rotate one quadrant to 90` ,but here itll cause dim issue so make it 180
    image[height//2:,:width//2]=smaller_frame
    image[:height//2,width//2:]=smaller_frame
    image[height//2:,width//2:]=smaller_frame

    cv2.imshow('frame',image)
    if cv2.waitKey(1) == ord('q'): #wait for 1 sec and check which key is pressed then break
        break

cap.release() #Release camera resource
cap.destroyAllWindows()