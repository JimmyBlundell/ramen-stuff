import numpy as np
import tensorflow as tf
from tensorflow import keras
import csv as csv

# Replace brand names that appear only once with "Other"

reader = csv.reader(open('ramen-ratings.csv', 'r'))
outputfile = open('variety.txt', 'w')

next(reader)

#Print each individual word into a separate file
for line in reader:
    for word in line[2].split():
        outputfile.write(word + '\n')
        print(word)


