# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:42:18 2017

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
from keras.layers.advanced_activations import PReLU
identifier = Sequential()
x = Input((64,64,1))
y = (Convolution2D(32,3,3,border_mode = "valid"))(x)
y = PReLU(init='zero', weights=None, shared_axes=None)(y)
y = (MaxPooling2D(pool_size = (2,2)))(y)
y = (Dropout(0.5))(y)
y = (Convolution2D(32,3,3,border_mode = "valid"))(y)
y = PReLU(init='zero', weights=None, shared_axes=None)(y)
y = (MaxPooling2D(pool_size = (2,2)))(y)
y = (Dropout(0.5))(y)
y = (Convolution2D(32,3,3,border_mode = "valid"))(y)
y = PReLU(init='zero', weights=None, shared_axes=None)(y)
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
identifier = Model(input =x, output = [digit1,digit2,digit3,digit4,digit5])
identifier.compile(optimizer = "RMSprop", loss = "sparse_categorical_crossentropy",metrics = ["accuracy"])
nb_epoch =10
identifier.fit(training_data.reshape(29329,64,64,1),label_list,batch_size= 64,nb_epoch= nb_epoch,
               verbose= 1,validation_data=(test_data.reshape(600,64,64,1),test_label_list))












