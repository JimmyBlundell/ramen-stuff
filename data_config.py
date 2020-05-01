import csv as csv
import numpy as np
from collections import Counter

#def configure_csv(oldFile, training_data, test_data, validation_data):

oldFile = "ramen-ratings.csv"
training_data = "training-data.csv"
test_data = "test-data.csv"
validation_data = "validation-data.csv"

reader = csv.reader(open(oldFile, 'r'))
data_len = len(list(reader))
reader = csv.reader(open(oldFile, 'r')) #Initializing again because I'm not sure how else to do it in the moment :)
next(reader)

#Create lists of words in varieties, styles, brands, and country
list_of_varieties = []
list_of_brands = []
list_of_styles = []
list_of_countries = []
for line in reader:
    for word in line[2].split():
        list_of_varieties.append(word)
    list_of_brands.append(line[1])
    list_of_styles.append(line[3])
    list_of_countries.append(line[4])

#Remove duplicates
list_of_brands = list(dict.fromkeys(list_of_brands))
list_of_styles = list(dict.fromkeys(list_of_styles))
list_of_countries = list(dict.fromkeys(list_of_countries))


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


#For later: map each element in lists to unique integer for later data processing
brandDict = {}
for i in range(len(list_of_brands)):
    brandDict[list_of_brands[i]] = i+1
brandDict["Other"] = len(brandDict) + 1

styleDict = {}
for i in range(len(list_of_styles)):
    styleDict[list_of_styles[i]] = i+1

countryDict = {}
for i in range(len(list_of_countries)):
    countryDict[list_of_countries[i]] = i+1

print(brandDict)
print(styleDict)
print(countryDict)


#Add brand names to string to keep track of # of occurrences using count() method
brand_names = ""
reader = csv.reader(open(oldFile, 'r'))
next(reader)

for line in reader:
    brand_names += line[1] + '\n'


#Edit csv, turning each line into list, then inserting back into csv
reader = csv.reader(open(oldFile, 'r'))
header = next(reader)

header[2] = "Variety1"
for i in range(100):
    header.insert(i+3, "Variety" + str(i+2))

print(header)

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
    lst[5] = float(lst[5])

    #All brands appearing once should be "Other"
    if (brand_names.count(lst[1]) == 1):
        lst[1] = "Other"
    lst[0] = str(lst[0])

    style = lst[3]
    country = lst[4]
    stars = lst[5]

    #TODO: Will this work with just regular array as I'm doing?
    array = list([0]*100)
    for word in line[2].split():
        if word in varietyDict:
            array[varietyDict[word]] += 1
    lst[2:101] = array

    lst.append(style)
    lst.append(country)
    lst.append(stars)

    #Create training, test, and validation sets, ignoring the "Top 10"
    if (count <= data_len*0.8):
        writer1.writerow(lst[0:104])
    elif (count <= data_len*0.9):
        writer2.writerow(lst[0:104])
    else:
        writer3.writerow(lst[0:104])

