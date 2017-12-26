# -*- coding: utf-8 -*- 
import os, re
import numpy as np
import random

from PIL import Image
from pickup_faces import pickup_face

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ALL_ACTRESS_COUNT = 2

class ConvertVector3:

    def __init__(self):
        self.datas = []
        self.labels = []
    
    def convertImageVector3to1(self, img):
        """
        3次元(100x100x3(RGB))から1次元に変換する
        """
        s = img.shape[0] * img.shape[1] * img.shape[2]
        img_vector3 = img.reshape(1, s)
    
        return img_vector3[0]
        
    def other_actor_random(self, actor_id):
        """
        乱数を生成してその他の女優を抽出
        """
        random_actor = actor_id
        while actor_id == random_actor:
            random_actor = random.randint(1,ALL_ACTRESS_COUNT)

        return random_actor
        
    def getVector3(self,id,c_label):
        """
        画像から3次元ベクトル(特徴量)を抽出する
        """
        
        ##
        # DBから女優名を引き出し、画像にアクセスして画像を引き出す
        ##
        
        name = '0000'+str(id)
        directory  = BASE_DIR+'/static/img/faces'
        
        files = [f for f in os.listdir(directory) if re.match(name, f)]
        
        for image in files:
            img_path = BASE_DIR+'/static/img/faces/'+image
            image_data = pickup_face(img_path)
            as_arrayed_img = np.asarray(image_data)

            # 好みの女優側
            # 3次元なのかを確認
            if (len(as_arrayed_img.shape) == 3):
                # RGBが3がどうか
                if (as_arrayed_img.shape[2] == 3):
                    self.datas.append(self.convertImageVector3to1(np.asarray(image_data)))
                    
                    # ラベル付を行う 1はYES
                    self.labels.append(c_label)
                    # labels.append(image.split("faces/target_")[1].split("-")[0].replace("reversed_", ""))


if __name__ == '__main__':

    test = ConvertVector3()
    test.getVector3(1,1)