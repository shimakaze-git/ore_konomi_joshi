# -*- coding: utf-8 -*-

import os
import cv2


def Square_areaSize(x, y, w, h):
    """
    四角形の面積
    """
    
    vertical = (x+w)-x
    side = (y+h)-y
    
    return vertical * side
    
def max_comparison(index, size, max_index, max_size):
    
    i, s = 0, 0
    if(max(size, max_size) == max_size):
        i = max_index
        s = max_size
    else:
        i = index
        s = size
    return i,s

def pickup_face(image_path):
    """
    真正面顔判定用のOpenCVファイルを使って、顔画像を切り出す
    """
    # カスケード分類器を読み込む(正面顔の検出分類器)
    cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
    
    # readimg
    image = cv2.imread(image_path)

    # grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = cascade.detectMultiScale(
        gray_image,
        minSize=(100, 100)
    )

    # Extract when just one face is detected
    if (len(faces) >= 1):
        
        max_size = 0
        max_index = 0
        
        for i in range(len(faces)):
            (x, y, w, h) = faces[i]
            size = Square_areaSize(x, y, w, h)
            max_index, max_size = max_comparison(i, size, max_index, max_size)
            
        (x, y, w, h) = faces[max_index]
        image = image[y:y+h, x:x+w]
        image = cv2.resize(image, (100, 100))
    else:
        image = None

    return image