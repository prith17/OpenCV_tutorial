import cv2

img=cv2.imread('img/dog.jpg',1) #1-mode

img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)#We can resize  to n*n by just changing in (,), if not then the keep it as (0,0) and then scale it like half by fx=0.5,fy=0.5

img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)


cv2.imwrite('img/new_img.jpg',img)#saving
#-1,cv2.IMREAD_COLOR: Loads a color image. Any transparency of image will be neglected. It is the default flag
# 0, cv2.IMREAD_GRAYSCALE: Loads image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED: Loads image as such including alpha channel

cv2.imshow('Image',img)#Image-label

#In colab
#from google.colab.patches import cv2_imshow
#cv2_imshow(img)




cv2.waitKey(0) #Wait for infinite time until a key is pressed and pass to next  line(If 5 then 5 secs)

cv2.destroyAllWindows() #We will not want the image to be loaded


