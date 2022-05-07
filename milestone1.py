from cmath import inf
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import os

####################################################################
#Functions for Augmentations


def resize(dir,path):
    plt.close()
    fig = plt.figure(figsize=(16, 8))
    imagePath = dir
    image = cv2.imread(imagePath)
    (h,w) = image.shape[:2]
    aspect = w/h
    os.chdir(path)
    for i in range(15):
        ratio = random.uniform(0.2,(1080/h))

        height = int(ratio * h) 
        width = int(height * aspect)

        dimension = (width,height)

        resizedImage = cv2.resize(image, dimension, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), resizedImage) 
        fig.add_subplot(3, 5, i+1)
        plt.imshow(resizedImage)

    plt.show()

def translate(dir,path):
    plt.close()
    fig = plt.figure(figsize=(16, 8))
    imagePath = dir
    image = cv2.imread(imagePath)
    (h,w) = image.shape[:2]
    os.chdir(path)
    for i in range(15):
        translationMatrix = np.float32([[1,0, random.randint(10,(w//3.3))],[0,1,random.randint(10,(h//2.67))]])
        movedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1],image.shape[0]))
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), movedImage)
        fig.add_subplot(3, 5, i+1)
        plt.imshow(movedImage)
    plt.show()
    
def rotate(dir,path):
    plt.close()
    fig = plt.figure(figsize=(16, 8))
    imagePath = dir
    image = cv2.imread(imagePath)
    center = tuple(np.array(image.shape[1::-1]) / 2)
    os.chdir(path)
    for i in range(15):
        angle = random.randint(-180,180)
        rotationMatrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotatedImage = cv2.warpAffine(image, rotationMatrix, (image.shape[1],image.shape[0]))
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), rotatedImage)
        fig.add_subplot(3, 5, i+1)
        plt.imshow(rotatedImage)
    plt.show()

def flip(dir,path):
    plt.close()
    fig = plt.figure(figsize=(16, 8))
    imagePath = dir
    image = cv2.imread(imagePath)
    os.chdir(path)
    for i in range(15):
        choice = random.randint(1,3)
        if choice == 1:
            flipped = cv2.flip(image, 1)
            cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), flipped)
            fig.add_subplot(3, 5, i+1)
            plt.imshow(flipped)
            #cv2.imshow("Flipped Horizontally", flipped)
        elif choice == 2:
            flipped = cv2.flip(image, 0) 
            cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), flipped)
            fig.add_subplot(3, 5, i+1)
            plt.imshow(flipped)
            #cv2.imshow("Flipped Vertically", flipped) 
        elif choice == 3:
            flipped = cv2.flip(image, -1) 
            cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), flipped)
            fig.add_subplot(3, 5, i+1)
            plt.imshow(flipped)
    plt.show()
     
def zoom(dir,path):
    plt.close()
    fig = plt.figure(figsize=(16, 8))
    imagePath = dir
    image = cv2.imread(imagePath)
    h = image.shape[0]
    os.chdir(path)
    for i in range(15):
        zoom_factor = random.uniform((1080/h),4)
        Zoomed = cv2.resize(image, None, fx=zoom_factor, fy=zoom_factor)
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), Zoomed)
        fig.add_subplot(3, 5, i+1)
        plt.imshow(Zoomed)
    plt.show()

        

