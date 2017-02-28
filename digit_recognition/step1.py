from idx2numpy import convert_from_file
import numpy as np
import matplotlib.pyplot as plt
#from sklearn import OneHotEncoding 
train_data = convert_from_file("trainX.idx")
train_labels = convert_from_file("train-labels.idx")
test_data = convert_from_file("t10k-images.idx3-ubyte.idx")
test_labels = convert_from_file("t10k-labels.idx1-ubyte.idx")
#create digit sequences
def CreateSeq(data,label,nn=6000):
    digits = np.empty((nn,28,28*5))
    labels = np.empty((nn,5))
    for i in range(nn):
        n = np.random.choice([2,3,4,5])
        idx = np.random.choice([x for x in range(10000)],n)
        digits_i = np.hstack(data[idx])
        labels_i = label[idx]
        if n<5:
            placeholder = np.zeros((28,(5-n)*28))
            digits_i = np.hstack((digits_i,placeholder))
            labels_i = np.hstack((labels_i,np.array([10]*(5-n))))
        digits[i] = digits_i
        labels[i] = labels_i
    return (digits,labels)    
        
seq,labels = CreateSeq(train_data,train_labels)
seq = seq.reshape(6000,28,140,1)/255
labels =labels.astype("uint8")
seq_test,labels_test = CreateSeq(train_data,train_labels)
seq_test=seq_test[0:600]/255
seq_test = seq_test.reshape(600,28,140,1)
labels_test = np.asarray(labels_test[0:600],dtype="uint8")
#%%
#create onehot encoding
from keras.utils import np_utils
coded_labels = np.empty((6000,55))
for ii in range(6000):
    oneHot = np.empty((5,11))    
    for k in range(5):
        
        oneHot[k] = np_utils.to_categorical(labels[ii][k],11)
    coded_labels[ii] = np.hstack(oneHot)
#%%
#create onehot encoding for test set
coded_labels_test = np.empty((600,55))
for ii in range(600):
    oneHot = np.empty((5,11))    
    for k in range(5):
        
        oneHot[k] = np_utils.to_categorical(labels_test[ii][k],11)
    coded_labels_test[ii] = np.hstack(oneHot)