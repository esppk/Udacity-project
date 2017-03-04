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
identifier = Sequential()
x = Input((28,140,1))
y = (Convolution2D(32,3,3,activation = "relu",border_mode = "valid"))(x)
y = (MaxPooling2D(pool_size = (2,2)))(y)
y = (Dropout(0.25))(y)
y= (Convolution2D(32,3,3,activation = "relu"))(y)
y = (MaxPooling2D(pool_size = (2,2)))(y)
#identifier.add(Dropout(0.25))
y = (Flatten())(y)
y =(Dense(output_dim = 256,activation = "relu"))(y)
y = (Dense(output_dim=128,activation = "relu"))(y)
digit1 = (Dense(output_dim =11,activation = "softmax"))(y)
digit2 = (Dense(output_dim =11,activation = "softmax"))(y)
digit3 = (Dense(output_dim =11,activation = "softmax"))(y)
digit4 = (Dense(output_dim =11,activation = "softmax"))(y)
digit5 = (Dense(output_dim =11,activation = "softmax"))(y)
identifier = Model(input =x, output = [digit1,digit2,digit3,digit4,digit5])
identifier.compile(optimizer = "adam", loss = "categorical_crossentropy",metrics = ["accuracy"])
nb_epoch =2
identifier.fit(seq,labels_list,batch_size= 128,nb_epoch= nb_epoch,
               verbose= 1,validation_data=(seq_test,labels_list_test))
#%%
# seperate labels to 5 arrays
#train labels
coded_label1 = coded_labels[:,0:11]
coded_label2 = coded_labels[:,11:22]
coded_label3 = coded_labels[:,22:33]
coded_label4 = coded_labels[:,33:44]
coded_label5 = coded_labels[:,44:55]
labels_list = [coded_label1,coded_label2,coded_label3,coded_label4,coded_label5]
#test labels
test_label1 = coded_labels_test[:,0:11]
test_label2 = coded_labels_test[:,11:22]
test_label3 = coded_labels_test[:,22:33]
test_label4 = coded_labels_test[:,33:44]
test_label5 = coded_labels_test[:,44:55]
labels_list_test = [test_label1,test_label2,test_label3,test_label4,test_label5]








