import cv2
import numpy as np
import random

imagePath = "images/lion.jpeg"
image = cv2.imread(imagePath)

####################################################################
#Functions for Augmentations

def resize(image):
    (h,w) = image.shape[:2]
    aspect = w/h
    
    ratio = random.uniform(0.2,(1080/h))

    height = int(ratio * h) 
    width = int(height * aspect)

    dimension = (width,height)

    resizedImage = cv2.resize(image, dimension, interpolation=cv2.INTER_CUBIC) 
    cv2.imshow("Resized Image", resizedImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def translate(image):
    (h,w) = image.shape[:2]
    translationMatrix = np.float32([[1,0, random.randint(10,(w//3.3))],[0,1,random.randint(10,(h//2.67))]])
    movedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1],image.shape[0]))
    cv2.imshow("Moved image", movedImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotate(image):
    (h,w) = image.shape[:2]
    center = (h//2, w//2)
    angle = random.randint(-180,180)
    rotationMatrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotatedImage = cv2.warpAffine(image, rotationMatrix, (image.shape[1],image.shape[0]))
    cv2.imshow("Rotated image", rotatedImage) 

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def flip(image):
    choice = random.randint(1,3)
    if choice == 1:
        flippedHorizontally = cv2.flip(image, 1)
        cv2.imshow("Flipped Horizontally", flippedHorizontally)
        cv2.waitKey(-1)
    elif choice == 2:
        flippedVertically = cv2.flip(image, 0) 
        cv2.imshow("Flipped Vertically", flippedVertically) 
        cv2.waitKey(-1)
    elif choice == 3:
        flippedHV = cv2.flip(image, -1) 
        cv2.imshow("Flipped H and V", flippedHV) 
        cv2.waitKey(-1)

    cv2.destroyAllWindows()

def zoom(img):
    zoom_factor = random.uniform(1.1,4)
    Zoomed = cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)
    cv2.imshow("Zoomed", Zoomed) 
    cv2.waitKey(-1)

    cv2.destroyAllWindows()
