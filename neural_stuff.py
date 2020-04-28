#import numpy as np
#import tensorflow as tf
#from tensorflow import keras
from data_config import configure_csv

oldFile = input("Name of csv file to be configured: ")
newFile = input("Name of new file to store processed data: ")

configure_csv(oldFile, newFile)
