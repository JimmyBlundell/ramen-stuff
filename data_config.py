
import csv as csv
from collections import Counter


def configure_csv(oldFile, training_data, test_data, validation_data):

    reader = csv.reader(open(oldFile, 'r'))
    data_len = len(list(reader))
    reader = csv.reader(open(oldFile, 'r')) #Initializing again because I'm not sure how else to do it in the moment :)
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
    reader = csv.reader(open(oldFile, 'r'))
    next(reader)

    for line in reader:
        brand_names += line[1] + '\n'


    #Edit csv, turning each line into list, then inserting back into csv
    reader = csv.reader(open(oldFile, 'r'))
    header = next(reader)

    writer1 = csv.writer(open(training_data, 'w'))
    writer2 = csv.writer(open(test_data, 'w'))
    writer3 = csv.writer(open(validation_data, 'w'))
    writer1.writerow(header)
    writer2.writerow(header)
    writer3.writerow(header)

    count = 0
    #Make new CSV file
    for line in reader:
        count += 1
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

        #Convert ratings to floats
        if (lst[5] == "Unrated"):
            continue
        lst[5] = float(lst[5])

        #Ignore Top Ten
        lst[6] = ""
        if (count <= data_len*0.8):
            writer1.writerow(lst)
        elif (count <= data_len*0.9):
            writer2.writerow(lst)
        else:
            writer3.writerow(lst)

