from tensorflow.keras.datasets import boston_housing
from tensorflow.keras import models, layers

# data loading
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

# data preprocessing
mean = train_data.mean(axis = 0)
std = train_data.std(axis = 0)
train_data -= mean
train_data /= std
test_data -= mean
test_data /= std

# model loading
model = models.Sequential()
model.add(layers.Dense(64, activation = 'relu', input_shape = (train_data.shape[1],)))
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dense(1))
model.summary()

# model compile
model.compile(optimizer = 'rmsprop', loss ='mse', metrics=['mae'])
history = model.fit(train_data, train_targets, epochs=100, batch_size = 4, validation_split = 0.2)

# model evaluate
test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
