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

#TODO: Not even sure if I'll use dataframes - may just convert csv to numpy arrays and pass those directly?
#TODO: ALternatively, perhaps I can go back and make dataframes from my new csv! Or, follow the 'directly from csv' tutorial altogether.

dataframe_training = pd.read_csv(training_data_csv)
dataframe_test = pd.read_csv(test_data_csv)
dataframe_validation = pd.read_csv(validation_data_csv)


dataframe_training['Brand'] = pd.Categorical(dataframe_training['Brand'])
dataframe_training['Brand'] = dataframe_training.Brand.cat.codes

dataframe_training['Style'] = pd.Categorical(dataframe_training['Style'])
dataframe_training['Style'] = dataframe_training.Style.cat.codes

dataframe_training['Country'] = pd.Categorical(dataframe_training['Country'])
dataframe_training['Country'] = dataframe_training.Country.cat.codes


training_target = dataframe_training.pop('Stars')
#Change target values to one-hot encoding
training_target = keras.utils.to_categorical(training_target)
validation_target = dataframe_validation.pop('Stars')
#Change target values to one-hot encoding
validation_target = keras.utils.to_categorical(validation_target)

training_dataset = tf.data.Dataset.from_tensor_slices((dataframe_training.values, training_target))
validation_dataset = tf.data.Dataset.from_tensor_slices((dataframe_validation.values, validation_target))

training_dataset = training_dataset.shuffle(len(dataframe_training)).batch(1)
validation_dataset = validation_dataset.shuffle(len(dataframe_validation)).batch(1)

def get_compiled_model():
  model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1),
    tf.keras.layers.Dense(1, activation='tanh') #Read somewhere tanh was superior to sigmoid so why not
  ])

  model.compile(optimizer='adam',
                loss=tf.keras.losses.MeanAbsoluteError(),
                metrics=['accuracy'])
  return model

model = get_compiled_model()
model.fit(training_dataset, batch_size=None, epochs=30, validation_data=(validation_dataset))



