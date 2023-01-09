import cv2
import random

img=cv2.imread('img/dog.jpg',1) #1-mode
print(img)#We get numpy array

print(img.shape)#Displays (height,width,channel)

#itll be in the following form=>(Blue,Green,Red):
# [[[0,0,0],[255,255,255]]]

# print(img[257][400])

#Modify image
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]


#Copy image
tag=img[500:600,400:500]#img[fromRow:toRow(not included), (in those rows)fromCol:toCol]
img[100:200,200:300]=tag #Copying must have same range in rows and columns while pasting as we copied i.e diff b/w 600-500=100 == 200-100


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()














