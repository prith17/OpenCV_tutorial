import numpy as np
import cv2

cap=cv2.VideoCapture(0) # Number of video devices i.e if we want to access 1st device or 1 or we can add video file too

while True:
    ret,frame=cap.read() # get frame(numpy array) and return value for that frame to check if proper
    width=int(cap.get(3))#Width of the video capture(There 17 diff properties)
    height=int(cap.get(4))#Height of the video capture(There 17 diff properties)
    image=np.zeros(frame.shape,np.uint8) #taking a dummy image

    img=cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    img=cv2.line(img,(0,height),(width,0),(0,255,0),10)

    #frame-source_image
    #(0,0)-starting position
    #(width,height)-ending
    #(255,0,0)-color
    #10-line_thickness

    img=cv2.rectangle(img,(100,100),(200,200),(128,128,128),5)

    #img-source_img
    #(100,100)-center_position
    #(200,200)-radius
    #(128,128,128)-colour
    #5-line_thickness(-1-some_number)

    img=cv2.circle(img,(300,300),60,(0,0,255),-1)
    #img-source_img
    #(300,300)-center_position
    #60-radius
    #(0,0,255)-colour
    #-1-line_thickness(-1-some_number)

    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(img,'Prithvi',(200,height-10),font,4,(0,0,0),5,cv2.LINE_AA)
    #img-souce_img
    #'Prithvi'-Text
    #(200, height - 10)-center_position
    #font
    #4-font_scale
    #(0, 0, 0)-color
    #5-line_thickness
    #cv2.LINE_AA-line_type


    #img-source_img
    #


    cv2.imshow('frame',img)
    if cv2.waitKey(1) == ord('q'): #wait for 1 sec and check which key is pressed then break
        break

cap.release() #Release camera resource
cap.destroyAllWindows()