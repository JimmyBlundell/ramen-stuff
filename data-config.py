#import numpy as np
#import tensorflow as tf
#from tensorflow import keras
import csv as csv
from collections import Counter

# Replace brand names that appear only once with "Other"

reader = csv.reader(open('ramen-ratings.csv', 'r'))

next(reader)

list_of_words = []

#Grab each individual word and put into separate list
for line in reader:
    for word in line[2].split():
        list_of_words.append(word)

#Create list of top 100 used words
counter = Counter(list_of_words)
top_hundred = counter.most_common(100)
print(top_hundred)

