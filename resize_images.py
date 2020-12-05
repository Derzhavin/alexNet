import PIL
from PIL import Image
import os


def resize_image(path_src, path_out, basewidth=227):
    img = Image.open(path_src)
    img = img.resize((basewidth, basewidth), PIL.Image.ANTIALIAS)
    img.save(path_out)


if __name__ == '__main__':
    os.chdir('sample')

    for dir in os.listdir():
        for img_file in os.listdir(dir):
            path = os.path.join(dir, img_file)
            resize_image(path, path)
            print(path)
