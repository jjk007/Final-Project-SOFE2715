import csv
import random


centriod = list()


def parse():
    "Parses the data sets from the csv file we are given to work with"
    file = open("exercise-4.csv")  # should be manualized later
    rawFile = csv.reader(file)    # Reading the csv file into a raw form
    rawData = list(rawFile)       # Converting the raw data into list from.
    return rawData


def cluster():
    "This is the main method, which executes k-means clustering algorithm"
    k = 3  # k is the number of clusters to be develped from the data
    newData = []
    data = parse()
    labels = data.pop(0)
    listSize = len(data)
    for i in range(0, listSize):  # Trying to convert the string list to float here
        newData.append([])        # Add a new sublsit every time
        for j in range(0, 2):
            newData[i].append(float(data[i][j]))  # Append converted data
    for i in range(0, 3):
        centriod.append(random.choice(newData))
    # These are the randomly picked centroids
    for i in range(0, 3):
        print centriod[i]
    print labels
    print newData


cluster()
