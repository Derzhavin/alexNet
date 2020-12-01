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
        self.session = tf.Session()
        self.base_width = 227
        self.classes = ['bee', 'wasp']

        saver = tf.train.Saver()
        saver.restore(self.session, 'tmp/checkpoints/model_epoch10.ckpt')

    def classify(self, src_img):
        w_percent = (self.base_width / float(src_img.size[0]))
        img_copy = src_img.resize((self.base_width, self.base_width), PIL.Image.ANTIALIAS)
        img_copy = np.array(img_copy)
        img_copy = img_copy.astype('float32')
        img_copy = np.reshape(img_copy, (1, 227, 227, 3))

        probs = self.session.run(self.softmax, feed_dict={self.x: img_copy, self.keep_prob: 1})
        prediction = self.classes[np.argmax(probs)]
        self.session.close()

        return prediction


if __name__ == '__main__':
    classifier = Classifier()

    img = Image.open("/home/denis/PycharmProjects/classifier/sample/bee/19150522_731d4e975b_m.jpg")
    print(classifier.classify(img))
