from net import Net
import numpy as np
import PIL
from PIL import Image
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


class Classifier(object):
    def __init__(self):
        self.x = tf.placeholder(tf.float32, [1, 227, 227, 3])
        self.keep_prob = tf.placeholder(tf.float32)
        self.model = Net(self.x, self.keep_prob, 2, [])
        self.softmax = tf.nn.softmax(self.model.fc8)
        self.classes = ['bee', 'wasp']
        self.session = tf.Session()
        self.base_width = 227

        saver = tf.train.Saver();
        saver.restore(self.session, 'tmp/checkpoints/model_epoch10.ckpt')

    def classify(self, src_img):
        w_percent = (self.base_width / float(src_img.size[0]))
        h_size = int((float(src_img.size[1] * float(w_percent))))
        img_copy = src_img.resize((self.base_width, self.base_width), PIL.Image.ANTIALIAS)
        img_copy = np.array(img_copy)
        img_copy = img_copy.astype('float32')
        img_copy = np.reshape(img_copy, (1, 227, 227, 3))

        probs = self.session.run(self.softmax, feed_dict={self.x: img_copy, self.keep_prob: 1})
        prediction = self.classes[np.argmax(probs)]

        return prediction


if __name__ == '__main__':
    classifier = Classifier()
    with open('./tables/test.txt', 'r') as f:
        paths = f.readlines()
        paths = list(map(lambda s: './' + s.strip()[:-2], paths))

    right_counter = 0
    raised_num = 0
    total = len(paths)
    for path in paths:
        img = Image.open(path)
        i = 9
        while path[i] != '/':
            i += 1
        answer = path[9:i]
        try:
            if answer == classifier.classify(img):
                right_counter += 1
        except:
            total -= 1
            raised_num += 1

    print(f'total num: {len(paths)}', )
    print(f'total num checked: {total}', )
    print(f'accuracy: {right_counter/total * 100}')
    print(f'num raised: {raised_num}')