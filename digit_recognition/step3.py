# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 03:58:36 2017

@author: Emrick
"""
#test new captured image

from skimage.data import imread
test_imag = imread("C:\\Users\\Emrick\\Documents\\Udacity projects\\Udacity-project\\digit_recognition\\79.jpg")

test_imag = np.mean(test_imag,axis = -1)/255
test_imag = resize(test_imag,(64,64))
a =identifier.predict(test_imag.reshape(1,64,64,1))