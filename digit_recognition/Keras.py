from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers.core import Dropout
identifier = Sequential()
identifier.add(Convolution2D(32,3,3,input_shape = (28,140,1),activation = "relu"))
identifier.add(MaxPooling2D(pool_size = (2,2)))
identifier.add(Dropout(0.2))
identifier.add(Convolution2D(32,3,3,activation = "relu"))
identifier.add(MaxPooling2D(pool_size = (2,2)))
identifier.add(Dropout(0.2))
identifier.add(Flatten())
identifier.add(Dense(output_dim = 256,activation = "relu"))
identifier.add(Dense(output_dim=128,activation = "relu"))
identifier.add(Dense(output_dim =55,activation = "softmax"))

identifier.compile(optimizer = "adam", loss = "categorical_crossentropy",metrics = ["accuracy"])
nb_epoch =25
identifier.fit(seq,coded_labels,batch_size= 60,nb_epoch= nb_epoch,
               verbose= 1,validation_data=(seq_test,coded_labels_test))
# print("Test score:",score[0])
# print("test accuracy:",score[1])
