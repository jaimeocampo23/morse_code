# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:12:11 2020

@author: jaime calderon
"""


from skimage import io, color
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras


a = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ES'])
x = np.size(a)
Muestras = 4
BDF = np.zeros([(x * Muestras), 43154])
for i in range(x):
    for j in range(Muestras):
        root = str(a[i]) + str(j + 1) + ".dat"
        Pic = np.loadtxt(root)
        BDF[((x * j) + i), :] = Pic.T

# ----------------------------------------------------------

xt = BDF
# xt=tf.keras.utils.normalize(BDF,axis = 1)

targ = np.tile(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                         18, 19, 20, 21, 22, 23, 24, 25, 26]), (1, Muestras)).T

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(150, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(27, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(xt, targ, epochs=200)  # train

loss, accuracy = model.evaluate(xt, targ)
print('Accuracy: %.2f' % accuracy)
print('Loss: %.2f' % loss)

model.save('Morse_Model.h5')
model.save_weights('Pesos_FM.h5')

# TrainedM=tf.keras.models.load_model('Face_Model.h5')
TrainedM = tf.keras.models.load_model('Morse_Model.h5')
Respu = TrainedM.predict(BDF)
