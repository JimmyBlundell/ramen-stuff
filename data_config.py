import csv as csv
import numpy as np
from collections import Counter

def configure_csv(oldFile, training_data, test_data, validation_data):

    oldFile = "ramen-ratings.csv"
    training_data = "training-data.csv"
    test_data = "test-data.csv"
    validation_data = "validation-data.csv"

    reader = csv.reader(open(oldFile, 'r'))
    data_len = len(list(reader))
    reader = csv.reader(open(oldFile, 'r')) #Need to condense all this in a whlie loop to avoid initializing the reader over and over
    next(reader)

    #Create lists of words in varieties
    list_of_varieties = []

    for line in reader:
        for word in line[2].split():
            list_of_varieties.append(word)


    #Create list of top 100 used words
    counter_words = Counter(list_of_varieties)
    counter_words = counter_words.most_common(100)
    list_of_varieties = []
    for word in counter_words:
        list_of_varieties.append(word[0])


    #Create dictionary mapping index to each word in top 100
    varietyDict = {}
    for i in range(0, 100):
        varietyDict[list_of_varieties[i]] = i


    #Add brand names to string to keep track of # of occurrences using count() method
    brand_names = ""
    reader = csv.reader(open(oldFile, 'r'))
    next(reader)

    for line in reader:
        brand_names += line[1] + '\n'


    #Edit csv, turning each line into list, then inserting back into csv
    reader = csv.reader(open(oldFile, 'r'))
    header = next(reader)

    #Remove review number, not important
    header.pop(0)

    #Create columns for 100 varieties - this is more for my sake than anything
    header[1] = "Variety1"
    for i in range(99):
        header.insert(i+2, "Variety" + str(i+2))

    writer1 = csv.writer(open(training_data, 'w'))
    writer2 = csv.writer(open(test_data, 'w'))
    writer3 = csv.writer(open(validation_data, 'w'))

    writer1.writerow(header[:-1])
    writer2.writerow(header[:-1])
    writer3.writerow(header[:-1])

    count = 0
    #Make new CSV file
    for line in reader:
        count += 1
        lst = list(line)

        #Convert ratings to floats, ignoring the few reviews that are unrated
        if (lst[5] == "Unrated"):
            continue

        #All brands appearing once should be "Other"
        if (brand_names.count(lst[1]) == 1):
            lst[1] = "Other"

        style = lst[3]
        country = lst[4]
        stars = float(lst[5])

        #Add all varietes as a frequency according to an index in an array (this is extending the columns of the csv file)
        array = list([0.0]*100)
        for word in line[2].split():
            if word in varietyDict:
                array[varietyDict[word]] += 1.0
        lst[2:101] = array

        #Add style, country, and stars back in
        lst.extend([style, country, stars])

        #Create training, test, and validation sets, ignoring the Review # and "Top 10"
        if (count <= data_len*0.8):
            writer1.writerow(lst[1:105])
        elif (count <= data_len*0.9):
            writer2.writerow(lst[1:105])
        else:
             writer3.writerow(lst[1:105])