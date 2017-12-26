# -*- coding: utf-8 -*- 
import os, re
import numpy as np

from PIL import Image
from pickup_faces import pickup_face

from convert_vector3 import ConvertVector3
from learn import learn

class WomanActressLearnning():
    
    def __init__(self, actress):
        
        # 女優リスト
        self.actress = actress
        
        self.datas = []
        self.labels = []
        
    def run(self):
        
        # インスタンスを生成
        converter = ConvertVector3()
        
        # 選択した女優のIDを入力していく
        for actor_id in self.actress:
            converter.getVector3(actor_id, 1)
            
        # 0のラベル付けをするための女優をランダムに選出
        for other_id in self.actress:
            other_actor = converter.other_actor_random(other_id)
            converter.getVector3(other_actor, 0)
            
        # データーとラベル
        self.datas = converter.datas
        self.labels = converter.labels
        
        # 教師データー(データー,ラベル)を与えてモデルを生成
        clf = learn(self.datas, self.labels)
        
        print(':',self.datas)
        print('-',self.labels)
        print(clf)
        
        
if __name__ == '__main__':

    actress = [ 1 ]
    
    actress_learnning = WomanActressLearnning(actress)
    actress_learnning.run()