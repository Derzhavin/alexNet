
from helper_functions import resize_image

import os

os.chdir('../tiny-imagenet-200/train')

i = 0

new_dirs = []
for dir in os.listdir():
     new_dirs += [os.path.join(dir, 'images')]

for dir in new_dirs:
     for img_file in os.listdir(dir):
          path = os.path.join(dir, img_file)
          resize_image(path, path)
          print(path)