import tensorflow 
from matplotlib import pyplot
from matplotlib.image import imread

folder = "images/train/"

for i in range(3):
  pyplot.subplot(330 + 1 + i)
  filename = folder + '/cat.' + str(i) + '.jpg'
  image = imread(filename)
  pyplot.imshow(image)
  pyplot.show()

for i in range(3):
  pyplot.subplot(330 + 1 + i)
  filename = folder + '/dog.' + str(i) + '.jpg'
  image = imread(filename)
  pyplot.imshow(image)
  pyplot.show()


from os import makedirs
from os import listdir
from os.path import join
from os.path import isfile
from shutil import copyfile
from random import seed
from random import random

dataset_home = 'images/'
subdirs = ['train/', 'test/']

for subdir in subdirs:
    labeldirs = ['dogs/', 'cats/']
    for labldir in labeldirs:
        newdir = dataset_home + subdir + labldir
        makedirs(newdir, exist_ok=True)

seed(1)
val_ratio = 0.25
src_directory = 'images/train'

for file in listdir(src_directory):
    src = join(src_directory, file)
    if isfile(src): 
        dst_dir = 'train/'
        if random() < val_ratio:
            dst_dir = 'test/'
        if file.startswith('cat'):
            dst = join(dataset_home, dst_dir, 'cats', file)
            copyfile(src, dst)
        elif file.startswith('dog'):
            dst = join(dataset_home, dst_dir, 'dogs', file)
            copyfile(src, dst)


from tensorflow.keras.optimizers import SGD
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout

def define_model():
    model = Sequential()
    model = Sequential()

    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', 
                     input_shape=(200, 200, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(1, activation='sigmoid'))
    
    opt = SGD(learning_rate=0.001, momentum=0.9)
    model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
    return model

model = define_model()


from tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(rescale=1.0/255.0)

batch_size = 64
train_it = datagen.flow_from_directory(dataset_home + 'train/',
    class_mode='binary', batch_size=64, target_size=(200, 200))
test_it = datagen.flow_from_directory(dataset_home + 'test/',
    class_mode='binary', batch_size=64, target_size=(200, 200))

import os

train_subdirs = os.listdir(dataset_home + 'train/')
test_subdirs = os.listdir(dataset_home + 'test/')

print("Train subdirectories:", train_subdirs)
print("Test subdirectories:", test_subdirs)

train_steps = len(train_it.classes) // batch_size
test_steps = len(test_it.classes) // batch_size

history = model.fit(train_it, steps_per_epoch=train_steps,
    validation_data=test_it, validation_steps=test_steps, epochs=20, verbose=0)

_, acc = model.evaluate(test_it, steps=len(test_it), verbose=0)
print('> %.3f' % (acc * 100.0),'%')