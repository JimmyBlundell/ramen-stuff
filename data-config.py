#import numpy as np
#import tensorflow as tf
#from tensorflow import keras
import csv as csv
from collections import Counter

# Replace brand names that appear only once with "Other"

reader = csv.reader(open('ramen-ratings.csv', 'r'))
new_data = csv.writer(open('new-data.csv', 'w'))

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

#Add brand names to string to keep track of # of occurrences
brand_names = ""
reader = csv.reader(open('ramen-ratings.csv', 'r'))
next(reader)

for line in reader:
    brand_names += line[1] + '\n'
print(brand_names)
'Use brand_names.count(brand) to iterate through original list and alter if needed'





#Edit csv, turning each line into list, then inserting back into csv
'''for line in reader:
    lst = list(line)
    print(lst)
'''



#


'''Now that I have a list of the top 100, I will go back through the csv,
# splitting the lines into words (like above), and checking each word for presence in top 100.
# I will create a new list out of said, and write that string to that particular row's index.
# OR: I can create a whole new csv file! Adding each word that matches a top 100
# to its particular location. This may be the better route. I also need to remove the last column (top 10).

Upon a little thought, this will be it:
Write to new csv:
    Write csv[0]
    Write csv[1]
    For csv[2]:
        create temp string
        temp_list = csv[2].split
        for item in list:
            if in top 100, temp_string += item
            (Figure out how to work with spaces here)
        Write string to csv[2]
    Continue for others, ignoring top 10.
    
As for brand names: Use map with key as brand, value as count. Search through, and increment each time if not found.
Then, go back through csv. Search all brand names again. If count == 1, change to other. Else, continue.
'''

