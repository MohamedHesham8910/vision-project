from cmath import inf
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import os

####################################################################
#Functions for Augmentations

def resize(dir,path):
    cv2.destroyAllWindows()
    imagePath = dir
    image = cv2.imread(imagePath)
    (h,w) = image.shape[:2]
    aspect = w/h
    os.chdir(path)
    for i in range(6):
        ratio = random.uniform(0.2,(1080/h))

        height = int(ratio * h) 
        width = int(height * aspect)

        dimension = (width,height)

        resizedImage = cv2.resize(image, dimension, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), resizedImage) 
        cv2.imshow("Resized Image", resizedImage)
        cv2.waitKey(500)

def translate(dir,path):
    cv2.destroyAllWindows()
    imagePath = dir
    image = cv2.imread(imagePath)
    (h,w) = image.shape[:2]
    os.chdir(path)
    for i in range(6):
        translationMatrix = np.float32([[1,0, random.randint(10,(w//3.3))],[0,1,random.randint(10,(h//2.67))]])
        movedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1],image.shape[0]))
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), movedImage)
        cv2.imshow("Moved image", movedImage)
        cv2.waitKey(500)
    
def rotate(dir,path):
    cv2.destroyAllWindows()
    imagePath = dir
    image = cv2.imread(imagePath)
    (h,w) = image.shape[:2]
    center = (h//2, w//2)
    os.chdir(path)
    for i in range(6):
        angle = random.randint(-180,180)
        rotationMatrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotatedImage = cv2.warpAffine(image, rotationMatrix, (image.shape[1],image.shape[0]))
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), rotatedImage)
        cv2.imshow("Rotated image", rotatedImage)
        cv2.waitKey(500)

def flip(dir,path):
    imagePath = dir
    image = cv2.imread(imagePath)
    os.chdir(path)
    for i in range(6):
        cv2.destroyAllWindows()
        choice = random.randint(1,3)
        if choice == 1:
            flipped = cv2.flip(image, 1)
            cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), flipped)
            cv2.imshow("Flipped Horizontally", flipped)
        elif choice == 2:
            flipped = cv2.flip(image, 0) 
            cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), flipped)
            cv2.imshow("Flipped Vertically", flipped) 
        elif choice == 3:
            flipped = cv2.flip(image, -1) 
            cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), flipped)
            cv2.imshow("Flipped H and V", flipped) 
            
        cv2.waitKey(500)
        
def zoom(dir,path):
    cv2.destroyAllWindows()
    imagePath = dir
    image = cv2.imread(imagePath)
    h = image.shape[0]
    os.chdir(path)
    for i in range(6):
        zoom_factor = random.uniform((1080/h),4)
        Zoomed = cv2.resize(image, None, fx=zoom_factor, fy=zoom_factor)
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), Zoomed)
        cv2.imshow("Zoomed", Zoomed)
        cv2.waitKey(500)
        

