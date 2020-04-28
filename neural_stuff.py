#import numpy as np
#import tensorflow as tf
#from tensorflow import keras
from data_config import configure_csv

oldFile = "ramen-ratings.csv"
training_data = "training_data.csv"
test_data = "test_data.csv"
validation_data = "validation-data.csv"

configure_csv(oldFile, training_data, test_data, validation_data)
