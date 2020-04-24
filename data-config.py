#import numpy as np
#import tensorflow as tf
#from tensorflow import keras
import csv as csv
from collections import Counter

# Replace brand names that appear only once with "Other"

reader = csv.reader(open('ramen-ratings.csv', 'r'))
next(reader)

#Grab each individual word and put into separate list
list_of_words = []
for line in reader:
    for word in line[2].split():
        list_of_words.append(word)


#Create list of top 100 used words
counter = Counter(list_of_words)
counter = counter.most_common(100)


#Add top 100 words to set for quicker access.
top_hundred = set({})
for word in counter:
    top_hundred.add(word[0])


#Add brand names to string to keep track of # of occurrences using count() method
brand_names = ""
reader = csv.reader(open('ramen-ratings.csv', 'r'))
next(reader)

for line in reader:
    brand_names += line[1] + '\n'


#Edit csv, turning each line into list, then inserting back into csv
reader = csv.reader(open('ramen-ratings.csv', 'r'))
header = next(reader)

writer = csv.writer(open('new-data.csv', 'w'))
writer.writerow(header)


#For reference: Review #,Brand,Variety,Style,Country,Stars,Top Ten
for line in reader:
    lst = list(line)
    #All brands appearing once should be "Other"
    if (brand_names.count(lst[1]) == 1):
        lst[1] = "Other"

    #Include only variety words in top 100
    temp = ""
    words = line[2].split()
    for i in range(len(words)):
        if (words[i] in top_hundred):
            if (len(temp.split()) == 0):
                temp += words[i]
            else:
                temp += ' ' + words[i]

    lst[2] = temp
    #Ignore Top Ten
    lst[6] = ""
    writer.writerow(lst)

