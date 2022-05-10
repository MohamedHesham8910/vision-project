import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import os

####################################################################
#Functions for Augmentations


def resize(path,dir,no):
    num = int(no)
    plt.close()
    fig = plt.figure(figsize=(16, 8))
    imagePath = path
    image = cv2.imread(imagePath)
    (h,w) = image.shape[:2]
    aspect = w/h
    os.chdir(dir)
    for i in range(num):
        ratio = random.uniform(0.2,(1080/h))

        height = int(ratio * h) 
        width = int(height * aspect)

        dimension = (width,height)

        resizedImage = cv2.resize(image, dimension, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), resizedImage) 
        fig.add_subplot(4, (num//4)+1, i+1)
        plt.imshow(resizedImage)

    plt.show()

def translate(path,dir,no):
    num = int(no)
    plt.close()
    fig = plt.figure(figsize=(16, 8))
    imagePath = path
    image = cv2.imread(imagePath)
    (h,w) = image.shape[:2]
    os.chdir(dir)
    for i in range(num):
        translationMatrix = np.float32([[1,0, random.randint(10,(w//3.3))],[0,1,random.randint(10,(h//2.67))]])
        movedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1],image.shape[0]))
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), movedImage)
        fig.add_subplot(4, (num//4)+1, i+1)
        plt.imshow(movedImage)
    plt.show()
    
def rotate(path,dir,no):
    num = int(no)
    plt.close()
    fig = plt.figure(figsize=(16, 8))
    imagePath = path
    image = cv2.imread(imagePath)
    center = tuple(np.array(image.shape[1::-1]) / 2)
    os.chdir(dir)
    for i in range(num):
        angle = random.randint(-180,180)
        rotationMatrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotatedImage = cv2.warpAffine(image, rotationMatrix, (image.shape[1],image.shape[0]))
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), rotatedImage)
        fig.add_subplot(4, (num//4)+1, i+1)
        plt.imshow(rotatedImage)
    plt.show()

def flip(path,dir,no):
    num = int(no)
    plt.close()
    fig = plt.figure(figsize=(16, 8))
    imagePath = path
    image = cv2.imread(imagePath)
    os.chdir(dir)
    for i in range(num):
        choice = random.randint(-1,1)
        flipped = cv2.flip(image, choice)
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), flipped)
        fig.add_subplot(4, (num//4)+1, i+1)
        plt.imshow(flipped)
    plt.show()
     
def zoom(path,dir,no):
    num = int(no)
    plt.close()
    fig = plt.figure(figsize=(16, 8))
    imagePath = path
    image = cv2.imread(imagePath)
    (h1,w1) = image.shape[:2]
    os.chdir(dir)
    for i in range(num):
        zoom_factor = random.uniform(1.2,2)
        zoomed = cv2.resize(image, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_CUBIC)
        (h2,w2) = zoomed.shape[:2]
        diff_h = (h2-h1)//2
        diff_w = (w2-w1)//2
        cropped = zoomed[ diff_h : h2 - diff_h , diff_w : w2 - diff_w]
        cv2.imwrite('New_Image{} .jpg'.format(random.randint(1,1000000000)), cropped)
        fig.add_subplot(4, (num//4)+1 , i+1)
        plt.imshow(cropped) 
    plt.show()

        

