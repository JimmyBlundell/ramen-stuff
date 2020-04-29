import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from data_config import configure_csv

oldFile = "ramen-ratings.csv"
training_data = "training-data.csv"
test_data = "test-data.csv"
validation_data = "validation-data.csv"

configure_csv(oldFile, training_data, test_data, validation_data)

dataframe_training = pd.read_csv(training_data)
dataframe_test = pd.read_csv(test_data)
dataframe_validation = pd.read_csv(validation_data)

#Function to make a tf dataset out of pandas dataframe
def make_tf_dataset(dataframe, shuffle=True, batch_size=43):
    dataframe = dataframe.copy()
    labels = dataframe.pop('Stars')
    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(dataframe))
    ds = ds.batch(batch_size)
    return ds

#training_ds = make_tf_dataset(dataframe_training, batch_size=43)
#test_ds = make_tf_dataset(dataframe_test, shuffle=False, batch_size=43)
#validation_ds = make_tf_dataset(validation_data, suffle=False, batch_size=43)






#label = 'Stars'


#batch_size = 32

#dataset = tf.data.experimental.make_csv_dataset(
#      training_data,
#      batch_size,
#      label_name=label,
#      na_value="?",
#      num_epochs=1,
#      ignore_errors=True,
#      )


#For my own purposes, visualizing the batches in my dataset
#for batch, label in dataset.take(1):
#    for key, value in batch.items():
#      print("{:2s}: {}".format(key,value.numpy()))

