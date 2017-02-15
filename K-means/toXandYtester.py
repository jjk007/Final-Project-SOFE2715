import csv
import random


centriod = list()
labels = ""
clusteredData = list()


def parse():
    "Parses the data sets from the csv file we are given to work with"
    file = open("exercise-4.csv")  # should be manualized later
    rawFile = csv.reader(file)    # Reading the csv file into a raw form
    rawData = list(rawFile)       # Converting the raw data into list from.
    return rawData

def toXandY(unorderedData):
    orderedData = []
    orderedData.append([])        # Add a new sublsit every time
    orderedData.append([])        # Add a new sublsit every time
    listSize = len(unorderedData)
    for x in range(0, listSize):
            orderedData[0].append(unorderedData[x][0])  # Seperates the x-cords
    for y in range(0, listSize):
            orderedData[1].append(unorderedData[y][1])  # Seperates the y-cords
    return orderedData



newData = []
data = parse()
labels = data.pop(0)
listSize = len(data)

for i in range(0, listSize):  # Converting the string list to float
    newData.append([])        # Add a new sublsit every time
    for j in range(0, 2):
        newData[i].append(float(data[i][j]))  # Append converted data
for i in range(0, 3):
    centriod.append(random.choice(newData))

newData = toXandY(newData)

print "All the x-cordinates"
print newData[0]
print "All the y-cordinates"
print newData[1]
