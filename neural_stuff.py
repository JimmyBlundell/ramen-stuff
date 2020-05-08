import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
#from keras.utils.np.utils import to_categorical
from data_config import configure_csv

oldFile = "ramen-ratings.csv"
training_data_csv = "training-data.csv"
test_data_csv = "test-data.csv"
validation_data_csv = "validation-data.csv"

configure_csv(oldFile, training_data_csv, test_data_csv, validation_data_csv)

dataframe_training = pd.read_csv(training_data_csv)
dataframe_test = pd.read_csv(test_data_csv)
dataframe_validation = pd.read_csv(validation_data_csv)


#Convert brand, style, and country columns to categories (one-hot baby)
dataframe_training['Brand'] = pd.Categorical(dataframe_training['Brand'])
dataframe_training['Brand'] = dataframe_training.Brand.cat.codes

dataframe_training['Style'] = pd.Categorical(dataframe_training['Style'])
dataframe_training['Style'] = dataframe_training.Style.cat.codes

dataframe_training['Country'] = pd.Categorical(dataframe_training['Country'])
dataframe_training['Country'] = dataframe_training.Country.cat.codes

dataframe_validation['Brand'] = pd.Categorical(dataframe_validation['Brand'])
dataframe_validation['Brand'] = dataframe_validation.Brand.cat.codes

dataframe_validation['Style'] = pd.Categorical(dataframe_validation['Style'])
dataframe_validation['Style'] = dataframe_validation.Style.cat.codes

dataframe_validation['Country'] = pd.Categorical(dataframe_validation['Country'])
dataframe_validation['Country'] = dataframe_validation.Country.cat.codes

dataframe_test['Country'] = pd.Categorical(dataframe_test['Country'])
dataframe_test['Country'] = dataframe_test.Country.cat.codes

dataframe_test['Brand'] = pd.Categorical(dataframe_test['Brand'])
dataframe_test['Brand'] = dataframe_test.Brand.cat.codes

dataframe_test['Style'] = pd.Categorical(dataframe_test['Style'])
dataframe_test['Style'] = dataframe_test.Style.cat.codes

dataframe_test['Country'] = pd.Categorical(dataframe_test['Country'])
dataframe_test['Country'] = dataframe_test.Country.cat.codes


training_target = dataframe_training.pop('Stars')
#Change target values to one-hot encoding
#training_target = keras.utils.to_categorical(training_target)

validation_target = dataframe_validation.pop('Stars')
#Change target values to one-hot encoding
#validation_target = keras.utils.to_categorical(validation_target)

test_target = dataframe_test.pop('Stars')
print(test_target)
#Change target values to one-hot encoding
#test_target=keras.utils.to_categorical(test_target)

#print(test_target)

training_dataset = tf.data.Dataset.from_tensor_slices((dataframe_training.values, training_target))
validation_dataset = tf.data.Dataset.from_tensor_slices((dataframe_validation.values, validation_target))
test_dataset = tf.data.Dataset.from_tensor_slices((dataframe_test.values, test_target))

training_dataset = training_dataset.shuffle(len(dataframe_training)).batch(1)
validation_dataset = validation_dataset.shuffle(len(dataframe_validation)).batch(1)


def get_compiled_model():
  model = tf.keras.Sequential([
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(1, activation='relu')
  ])

  model.compile(optimizer='adam',
                loss=tf.keras.losses.MeanSquaredError(),
                metrics=['mean_squared_error'])
  return model

model = get_compiled_model()
model.fit(training_dataset, batch_size=None, epochs=10, validation_data=(validation_dataset))

#TODO: This is a TensorSliceDataset. I need to reshape this, or figure out how to, in order for model.evaluate to work
#test_loss, test_accuracy = model.evaluate(test_dataset)

#print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))