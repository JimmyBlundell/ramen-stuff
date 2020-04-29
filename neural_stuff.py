import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
from data_config import configure_csv

oldFile = "ramen-ratings.csv"
training_data = "training_data.csv"
test_data = "test_data.csv"
validation_data = "validation-data.csv"

configure_csv(oldFile, training_data, test_data, validation_data)


label = 'Stars'


batch_size = 32

dataset = tf.data.experimental.make_csv_dataset(
      training_data,
      batch_size, # Artificially small to make examples easier to show.
      label_name=label,
      na_value="?",
      num_epochs=1,
      ignore_errors=True,
      )

#For my own purposes, visualizing the batches in my dataset
for batch, label in dataset.take(1):
    for key, value in batch.items():
      print("{:2s}: {}".format(key,value.numpy()))