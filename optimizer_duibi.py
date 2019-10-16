# -*- coding: utf-8 -*-
"""
@author: kemu
"""
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
def reset_graph(seed=42):
    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.seed(seed)
reset_graph()
plt.figure(1,figsize=(10,8))
x = np.linspace(-1,1,100)[:,np.newaxis] #<==>x=x.reshape(100,1)
noise = np.random.normal(0,0.1,size = x.shape)
y=np.power(x,2) + x +noise #y=x^2 + x+噪音
plt.scatter(x,y)
plt.show()
learning_rate = 0.01
batch_size = 10 #mini-batch的大小
class Network(object):
    def __init__(self,func,**kwarg):
        self.x = tf.placeholder(tf.float32,[None,1])
        self.y = tf.placeholder(tf.float32,[None,1])
        hidden = tf.layers.dense(self.x,20,tf.nn.relu)
        output = tf.layers.dense(hidden,1)
        self.loss = tf.losses.mean_squared_error(self.y,output)
        self.train = func(learning_rate,**kwarg).minimize(self.loss)
SGD = Network(tf.train.GradientDescentOptimizer)
Momentum = Network(tf.train.MomentumOptimizer,momentum=0.5)
AdaGrad = Network(tf.train.AdagradOptimizer)
RMSprop = Network(tf.train.RMSPropOptimizer)
Adam = Network(tf.train.AdamOptimizer)
networks = [SGD,Momentum,AdaGrad,RMSprop,Adam]
record_loss = [[], [], [], [], []] #踩的坑不能使用[[]]*5
plt.figure(2,figsize=(10,8))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for stp in range(200):
        index = np.random.randint(0,x.shape[0],batch_size)#模拟batch
        batch_x = x[index]
        batch_y = y[index]
        for net,loss in zip(networks,record_loss):
            _,l = sess.run([net.train,net.loss],feed_dict={net.x:batch_x,net.y:batch_y})
            loss.append(l)#保存每一batch的loss
labels = ['SGD','Momentum','AdaGrad','RMSprop','Adam']
for i,loss in enumerate(record_loss):
    plt.plot(loss,label=labels[i])
plt.legend(loc="best")
plt.xlabel("steps")
plt.ylabel("loss")
plt.show()