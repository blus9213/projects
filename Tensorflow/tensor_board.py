import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPool2D
import pickle
import datetime

# TensorBoard setup


# sess.graph contains the graph definition; that enables the Graph Visualizer.


# GPU memory configuration
from tensorflow.compat.v1 import ConfigProto, InteractiveSession
config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.333
session = InteractiveSession(config=config)

# Load data
X = pickle.load(open("X.pickle", "rb"))
y = pickle.load(open("Y.pickle", "rb"))

# Normalize data
X = X / 255.0

# Model
model = Sequential()

# Layer 1
model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPool2D(pool_size=(2, 2)))

# Layer 2
model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPool2D(pool_size=(2, 2)))

# Fully connected layers
model.add(Flatten())
model.add(Dense(64))

# Output layer
model.add(Dense(1))
model.add(Activation("sigmoid"))

# Compile model
model.compile(loss='binary_crossentropy', 
              optimizer='adam',
              metrics=['accuracy'])


log_dir = "my_logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)

model.fit(X, y, batch_size=32, epochs=2, validation_split=0.1, callbacks=[tensorboard_callback])
