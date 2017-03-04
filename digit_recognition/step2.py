# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 01:33:31 2017

@author: Emrick
"""

    
#%%
#set data set size
nn=10854
#%%

import numpy as np
#import os
#import tarfile
#import urllib
#from IPython.display import display, Image
#from scipy import ndimage
import h5py

train_filename = 'SVHN/train/digitStruct.mat'
f = h5py.File("C:/Users/Emrick/Documents/Udacity projects/train/digitStruct.mat")

metadata= {}
metadata['height'] = []
metadata['label'] = []
metadata['left'] = []
metadata['top'] = []
metadata['width'] = []

def print_attrs(name, obj):
    vals = []
    if obj.shape[0] == 1:
        vals.append(obj[0][0])
    else:
        for k in range(obj.shape[0]):
            vals.append(f[obj[k][0]][0][0])
    metadata[name].append(vals)
    

for item in f['/digitStruct/bbox']:
    f[item[0]].visititems(print_attrs)
    
#%%

# convert label to array
train_labels = []
for label in metadata["label"]:
    
    temp = np.zeros((5))
    for i in range(len(label)):
        temp[i] = label[i]
    train_labels.append(temp)
#%%
train_labels = np.array(train_labels,dtype = "uint8")
#%%
#set a test labels with onehot encoding
test_labels = train_labels[:600]
training_labels = train_labels[600:]
#%%
label_list = [training_labels[:,0],
              training_labels[:,1],
              training_labels[:,2],
              training_labels[:,3],
              training_labels[:,4]]
test_label_list = [test_labels[:,0],
                    test_labels[:,1],
                    test_labels[:,2],
                    test_labels[:,3],
                    test_labels[:,4]
                    ]

#%%
#OneHot encoding the labels
from keras.utils import np_utils
coded_labels = np.empty((nn,55))
for ii in range(nn):
    oneHot = np.empty((5,11))    
    for k in range(5):
        oneHot[k] = np_utils.to_categorical(train_labels[ii][k],11)
    coded_labels[ii] = np.hstack(oneHot)
#%%
#seperate the labels 
coded_label1 = coded_labels[:nn,0:11]
coded_label2 = coded_labels[:nn,11:22]
coded_label3 = coded_labels[:nn,22:33]
coded_label4 = coded_labels[:nn,33:44]
coded_label5 = coded_labels[:nn,44:55]
labels_list = [coded_label1,coded_label2,coded_label3,coded_label4,coded_label5]


#%%
#load the pictures
from skimage.data import imread
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt

train_data = []
for i in range(29929):
    path = "C:\\Users\\Emrick\\Documents\\Udacity projects\\train\\"
    path = path +str(i+1)+".png"
    pic = np.mean(imread(path),axis = -1)
    pic = resize(pic,(64,64))
    train_data.append(pic)
#%%        
train_data = np.array(train_data)
#%%
#set aside a testing set 
test_data = train_data[:600]
training_data = train_data[600:]
#%%
test_labels = []
for labels in labels_list:  
    test_label = labels[:600]
    test_labels.append(test_label)
train_labels = []
for labels in labels_list:
    train_label = labels[600:]
    train_labels.append(train_label)

#%%
#get the number using bbox
top = metadata["top"][0][0]
bottom = top + metadata["height"][0][0]
left = metadata["left"][0][0]
right = left + metadata["width"][0][0]
num = p[top:bottom,left:right]
plt.imshow(num,cmap = "gray")
plt.show()

#%%
#cropping number as a whole
from skimage.data import imread
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import resize
from skimage import filters
from skimage.exposure import adjust_gamma
train_data_cropped = []
for i in range(29929):
#    pic = imread("C:\\Users\\Emrick\\Documents\\Udacity projects\\train\\1109.png")
#    pic = np.mean(pic,axis = -1)
    #i = 1108
    path = "C:\\Users\\Emrick\\Documents\\Udacity projects\\train\\"
    path = path +str(i+1)+".png"
    pic = np.mean(imread(path),axis = -1)/255
    height =[]
    top = []
    bottom = []
    for k in range(len(metadata["height"][i])):
        height.append(metadata["height"][i][k])
        top.append(metadata["top"][i][k])
        bottom.append(metadata["top"][i][k]+metadata["height"][i][k])
    k = len(metadata["height"][i])
    top = min(top)
    bottom = max(bottom)
    right = metadata["left"][i][k-1] + metadata["width"][i][k-1]
    left = metadata["left"][i][0]
    width = right - left
    #left -= 0.15*width
    left = int([0,left][left>0])
    #right += 0.15*width
    right = int([0,right][right>0])
    height = bottom - top
    #top -= 0.15*height
    top = int([0,top][top>0])
    #bottom += 0.5*height
    bottom = int([0,bottom][bottom>0])
    p = pic[top:bottom,left:right]
    #binormial segementation
    #p= filters.threshold_adaptive(p,block_size = 31)
    
    #padded_pic = np.ones((28,140),dtype = "float32")
    p = np.ascontiguousarray(resize(p,(64,64)))
    #padded_pic[:,:int(140/5*k)] = p
    train_data_cropped.append(p)
#%%    
train_data_cropped = np.array(train_data_cropped)
   
#%%
#crop the picture

p = pic[top:bottom,left:right]
plt.imshow(p,cmap = "gray")
plt.show()    
    
#%%
#resize picture 
from skimage.transform import resize
padded_pic = 255*np.ones((28,140),dtype = "float32")
p = resize(p,(28,int(140/5*k)))
padded_pic[:,:int(140/5*k)] = p
padded_pic /=255
plt.imshow(padded_pic,cmap = "gray")
plt.show()    
#%%
#binary segmentation
from skimage import filters
pic = imread("C:\\Users\\Emrick\\Documents\\Udacity projects\\train\\9.png")
pic = np.mean(pic,axis = -1)/3
i=8
height =[]
top = []
bottom = []
for k in range(len(metadata["height"][i])):
    height.append(metadata["height"][i][k])
    top.append(metadata["top"][i][k])
    bottom.append(metadata["top"][i][k]+metadata["height"][i][k])
k = len(metadata["height"][i])
top = min(top)
bottom = max(bottom)
right = metadata["left"][i][k-1] + metadata["width"][i][k-1]
left = metadata["left"][i][0]
width = right - left
#left -= 0.1*width
left = int([0,left][left>0])
#right += 0.15*width
right = int([0,right][right>0])
height = bottom - top
#top -= 0.1*height
top = int([0,top][top>0])
#bottom += 0.5*height
bottom = int([0,bottom][bottom>0])
p = pic[top:bottom,left:right]

#from skimage.exposure import adjust_gamma
#        
#v= filters.threshold_li(p ) 
#p1=p>v
#plt.imshow(p1,cmap = "gray")
plt.imshow(filters.threshold_adaptive(p,block_size = 31),cmap = "gray") 
#%%
#test
pic = imread("C:\\Users\\Emrick\\Documents\\Udacity projects\\train\\25.png")
pic = np.mean(pic,axis = -1)/3
i=24
height =[]
top = []
bottom = []
for k in range(len(metadata["height"][i])):
    height.append(metadata["height"][i][k])
    top.append(metadata["top"][i][k])
    bottom.append(metadata["top"][i][k]+metadata["height"][i][k])
k = len(metadata["height"][i])
top = min(top)
bottom = max(bottom)
right = metadata["left"][i][k-1] + metadata["width"][i][k-1]
left = metadata["left"][i][0]
width = right - left
#left -= 0.15*width
left = int([0,left][left>0])
#right += 0.15*width
right = int([0,right][right>0])
height = bottom - top
#top -= 0.15*height
top = int([0,top][top>0])
#bottom += 0.5*height
bottom = int([0,bottom][bottom>0])
p = pic[top:bottom,left:right]
#binormial segementation
p= filters.threshold_adaptive(p , block_size = 15 ) 
padded_pic = np.ones((28,140),dtype = "float32")
p = resize(p,(28,int(140/5*k)))
padded_pic[:,:int(140/5*k)] = p
plt.imshow(padded_pic,cmap="gray")
#%%
train_data = []

    