import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from data_config import configure_csv

oldFile = "ramen-ratings.csv"
training_data_csv = "training-data.csv"
test_data_csv = "test-data.csv"
validation_data_csv = "validation-data.csv"

configure_csv(oldFile, training_data_csv, test_data_csv, validation_data_csv)

#TODO: Not even sure if I'll use dataframes - may just convert csv to numpy arrays and pass those directly?

dataframe_training = pd.read_csv(training_data_csv)
dataframe_test = pd.read_csv(test_data_csv)
dataframe_validation = pd.read_csv(validation_data_csv)


dataframe_training['Brand'] = pd.Categorical(dataframe_training['Brand'])
dataframe_training['Brand'] = dataframe_training.Brand.cat.codes

dataframe_training['Style'] = pd.Categorical(dataframe_training['Style'])
dataframe_training['Style'] = dataframe_training.Style.cat.codes

dataframe_training['Country'] = pd.Categorical(dataframe_training['Country'])
dataframe_training['Country'] = dataframe_training.Country.cat.codes


#target = dataframe_training.pop('Stars')
#training_dataset = tf.data.Dataset.from_tensor_slices((dataframe_training.values, target.values))

#for feat, targ in training_dataset.take(5):
#  print ('Features: {}, Target: {}'.format(feat, targ))

#print(dataframe_training.head(10))
#print(dataframe_training.dtypes)


#Function to make a tf dataset out of pandas dataframe - Not sure if I need at the moment!
#def make_tf_dataset(dataframe, shuffle=True, batch_size=43):
#    dataframe = dataframe.copy()
#    labels = dataframe.pop('Stars')
#    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
#    if shuffle:
#        ds = ds.shuffle(buffer_size=len(dataframe))
#    ds = ds.batch(batch_size)
#    return ds

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

