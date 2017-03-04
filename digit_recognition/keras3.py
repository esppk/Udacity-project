# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 03:02:39 2017

@author: Emrick
"""

from keras.models import Sequential
from keras.models import Model
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Input
from keras.layers.core import Dropout
identifier = Sequential()
x = Input((64,64,1))
y = (Convolution2D(32,3,3,activation = "relu",border_mode = "valid"))(x)
y = (MaxPooling2D(pool_size = (2,2)))(y)
y = (Convolution2D(64,3,3,activation = "relu",border_mode = "valid"))(x)
y = (MaxPooling2D(pool_size = (2,2)))(y)
y = (Dropout(0.5))(y)
y= (Convolution2D(128,3,3,activation = "relu"))(y)
y = (MaxPooling2D(pool_size = (2,2)))(y)
y = (Dropout(0.5))(y)
y= (Convolution2D(256,3,3,activation = "relu"))(y)
y = (MaxPooling2D(pool_size = (2,2)))(y)
y = (Dropout(0.5))(y)

y = (Flatten())(y)
y =(Dense(output_dim = 512,activation = "relu"))(y)
#y = (Dense(output_dim=256,activation = "relu"))(y)
y = (Dense(output_dim=256,activation = "relu"))(y)
y = (Dense(output_dim=128,activation = "relu"))(y)
digit1 = (Dense(output_dim =11,activation = "softmax"))(y)
digit2 = (Dense(output_dim =11,activation = "softmax"))(y)
digit3 = (Dense(output_dim =11,activation = "softmax"))(y)
digit4 = (Dense(output_dim =11,activation = "softmax"))(y)
digit5 = (Dense(output_dim =11,activation = "softmax"))(y)
left1 = (Dense(output_dim =1,activation = "linear"))(y)
left2 = (Dense(output_dim =1,activation = "linear"))(y)
left3 = (Dense(output_dim =1,activation = "linear"))(y)
left4 = (Dense(output_dim =1,activation = "linear"))(y)
left5 = (Dense(output_dim =1,activation = "linear"))(y)
height1 = (Dense(output_dim =1,activation = "linear"))(y)
height2 = (Dense(output_dim =1,activation = "linear"))(y)
height3 = (Dense(output_dim =1,activation = "linear"))(y)
height4 = (Dense(output_dim =1,activation = "linear"))(y)
height5 = (Dense(output_dim =1,activation = "linear"))(y)
top1 = (Dense(output_dim =1,activation = "linear"))(y)
top2 = (Dense(output_dim =1,activation = "linear"))(y)
top3 = (Dense(output_dim =1,activation = "linear"))(y)
top4 = (Dense(output_dim =1,activation = "linear"))(y)
top5 = (Dense(output_dim =1,activation = "linear"))(y)
width1 = (Dense(output_dim =1,activation = "linear"))(y)
width2 = (Dense(output_dim =1,activation = "linear"))(y)
width3= (Dense(output_dim =1,activation = "linear"))(y)
width4 = (Dense(output_dim =1,activation = "linear"))(y)
width5 = (Dense(output_dim =1,activation = "linear"))(y)
regression = Model(input = x,output = [left1,left2,left3,left4,left5,
                                       height1,height2,height3,height4,height5,
                                       top1,top2,top3,top4,top5,
                                       width1,width2,width3,width4,width5])
regression.compile(optimizer = "adam", loss = "mean_squared_error",metrics = ["accuracy"] )
identifier = Model(input =x, output = [digit1,digit2,digit3,digit4,digit5])
identifier.compile(optimizer = "adam", loss = "categorical_crossentropy",metrics = ["accuracy"])
nb_epoch =10
identifier.fit(training_data.reshape(29329,64,64,1),train_labels,batch_size= 64,nb_epoch= nb_epoch,
               verbose= 1,validation_data=(test_data.reshape(600,64,64,1),test_labels))
regression.fit(training_data.reshape(29929,64,64,1),reg_labels,batch_size= 64,nb_epoch= nb_epoch,
               verbose= 1)