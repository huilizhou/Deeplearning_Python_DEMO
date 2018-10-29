# coding=utf-8

import tensorflow as tf
import numpy as np
import pdb
from datetime import datetime
from VGG16 import *
import cv2
import os
from PIL import Image
from scipy import ndimage


class chenvgg16_convol(object):

    def __init__(self):
        self.batch_size = 1
        self.test_num = np.zeros([1, 96, 96, 3], dtype=np.float32)
        self.image_holder = tf.placeholder(
            tf.float32, [self.batch_size, 96, 96, 3])
        self.label_holder = tf.placeholder(tf.int32, [self.batch_size])

        self.x = tf.placeholder(dtype=tf.float32, shape=[
            1, 224, 224, 3], name='input')
        self.keep_prob = tf.placeholder(tf.float32)
        self.output = VGG16(self.x, self.keep_prob, 10)
        self.score = tf.nn.softmax(self.output)
        self.f_cls = tf.argmax(self.score, 1)

        # self.sess = tf.InteractiveSession()
        self.sess = tf.Session()
        self.saver = tf.train.Saver()
        self.sess.run(tf.global_variables_initializer())
        self.saver.restore(self.sess, './model/model.ckpt-9999')

    def recognpic(self, pic):
        # batch_size = 1
        # test_num = np.zeros([1, 96, 96, 3], dtype=np.float32)
        # image_holder = tf.placeholder(tf.float32, [batch_size, 96, 96, 3])
        # label_holder = tf.placeholder(tf.int32, [batch_size])

        # sess = tf.InteractiveSession()
        # sess.run(tf.global_variables_initializer())
        # saver = tf.train.Saver()
        # saver.restore(sess, './model/model.ckpt-9999')
        # for i in os.listdir(path):
        #     imgpath = os.path.join(path, i)
        #     im = cv2.imread(imgpath)
        #     im = cv2.resize(im, (224, 224))  # * (1. / 255)
        pic = np.expand_dims(pic, axis=0)
        pred = self.sess.run(self.f_cls, feed_dict={
                             self.x: pic, self.keep_prob: 1.0})

        return pred
        # pred, _score = sess.run([f_cls, score], feed_dict={
        #     x: pic, keep_prob: 1.0})
        #     prob = round(np.max(_score), 4)
        #     # print ("{} flowers class is: {}".format(i, pred))
        #     print("{} fruits class is: {}, score: {}".format(i, int(pred), prob))


if __name__ == '__main__':
    path = './test'
    test(path)
