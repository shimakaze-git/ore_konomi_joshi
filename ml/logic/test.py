# -*- coding: utf-8 -*- 
import os
import re
from PIL import Image


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# files = ["faces/" + f for f in os.listdir("faces") if re.match("target_", f)]
print(os.listdir())
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR.listdir('statics'))
print(os.listdir(BASE_DIR+'/static/img/faces'))

files = [f for f in os.listdir(BASE_DIR+'/static/img/faces') if re.match("00001_", f)]
print(files)