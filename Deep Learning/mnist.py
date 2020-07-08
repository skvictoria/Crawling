import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# data loading
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


# data preprocessing
train_images = train_images.reshape((60000, 28*28))
test_images = test_images.reshape((10000, 28*28))


# one-hot encoding
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# model loading
model = models.Sequential()
model.add(layers.Dense(units = 512,activation = 'relu', input_shape = (28*28, )))
model.add(layers.Dense(units = 10, activation='softmax'))
model.summary()
'''

# model loading if not reshaping
model = models.Sequential()
model.add(layers.Flatten(input_shape = (28, 28)))
model.add(layers.Dense(units = 512, activation = 'relu'))
model.add(layers.Dense(units = 10, activation = 'softmax'))
model.summary()

'''
# model compile
model.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(train_images, train_labels, epochs=30, batch_size=128, validation_split=0.2)
'''
# model compile_if not onehot encoding
model.compile(optimizer = 'rmsprop', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(train_images, train_labels, epochs=30, batch_size=128, validation_split=0.2)
'''
# model evaluate
test_loss, test_acc = model.evaluate(x = test_images, y = test_labels)
predict = model.predict(test_images[0].reshape((1, 28*28)))

print('predict probability : ', predict)
print('predict number : ', np.argmax(predict))

plt.figure()
plt.imshow(test_images[0].reshape(28, 28)*255)
plt.show()
