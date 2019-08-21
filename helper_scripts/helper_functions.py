# -*- coding: utf-8 -*-
from typing import Optional, Any

import PIL
from PIL import Image

def resize_image(pathTo, pathOut, basewidth=227):
    img = Image.open(pathTo)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1]*float(wpercent))))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(pathOut)
