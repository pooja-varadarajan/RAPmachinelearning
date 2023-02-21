import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from keras.datasets import mnist
from matplotlib import pyplot as plt
import cv2
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape)

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
print(x_train.shape)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print(y_train.shape)
print(y_train[:10])

from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)
print(y_train.shape)
print(y_train)

model = Sequential()
model.add(Conv2D(28, kernel_size=(3,3), activation = 'relu', input_shape = (28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation = 'relu'))
model.add(Dense(10,activation = 'softmax'))

model.compile(optimizer='adam', loss = 'mean_squared_error', metrics=['accuracy'])

model.fit(x_train, y_train, epochs = 20)

img = cv2.imread('IMAGEEEEEEE')

img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray.shape

img=cv2.resize(gray,(28,28))

img.shape

img = tf.keras.utils.normalize(img, axis = 1)

img = np.array(img).reshape(1, 28, 28,1)

#image_index = 5555
#plt.imshow(img) #plt is not used for 4D images
pred = model.predict(img)
print(pred.argmax())
print(np.argmax(pred[0]))
