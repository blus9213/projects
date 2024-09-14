import tensorflow as tf
import numpy as np
import keras
model = keras.Sequential([keras.layers.Dense(units=1, input_shape =[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')
# this is machine learning{using to guess y = f(x)}
xs = np.array([-1.0, 0.0, 1.0,2.0],dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0],dtype=float)

model.fit(xs,ys, epochs=150)

print(model.predict(np.array([1.0])))