# thou shall not cross 80 columns in thy file

import csv
import random
import math
import matplotlib.pyplot as plot


centriod = list()
clustered = list()


def cluster():
    "This is the main method, which executes k-means clustering algorithm"
    k = 3  # k is the number of clusters to be develped from the data
    newData = []
    data = parse()
    labels = data.pop(0)
    listSize = len(data)
    clustered.append([])
    clustered.append([])
    clustered.append([])

    for i in range(0, listSize):  # Converting the string list to float
        newData.append([])        # Add a new sublsit every time
        for j in range(0, 2):
            newData[i].append(float(data[i][j]))  # Append converted data
    for i in range(0, 3):
        centriod.append(random.choice(newData))
    # These are the randomly picked centroids, should be calculated later

    for val in newData:
        distance1 = euclideanDistance(centriod[0], val)
        distance2 = euclideanDistance(centriod[1], val)
        distance3 = euclideanDistance(centriod[2], val)
        if(distance1 > distance2 and distance1 > distance3):
            clustered[0].append(val)
        elif(distance2 > distance1 and distance2 > distance3):
            clustered[1].append(val)
        else:
            clustered[2].append(val)

    clustered[0] = toXandY(clustered[0])
    clustered[1] = toXandY(clustered[1])
    clustered[2] = toXandY(clustered[2])
    draw(clustered[0][0], clustered[0][1],labels[0], labels[1], "Cluster1", "r")
    draw(clustered[1][0], clustered[1][1],labels[0], labels[1], "Cluster2", "g")
    draw(clustered[2][0], clustered[2][1],labels[0], labels[1], "Cluster3", "b")


def euclideanDistance(p, q):
    "This calculates the Euclidean Distance b/w p & q, in the standard way"
    distance = math.sqrt(((p[0]-q[0])**2) + ((p[1]-q[1])**2))
    return distance


def parse():
    "Parses the data sets from the csv file we are given to work with"
    file = open("exercise-3.csv")  # should be manualized later
    rawFile = csv.reader(file)    # Reading the csv file into a raw form
    rawData = list(rawFile)       # Converting the raw data into list from.
    return rawData
    '''
    Remember, csv reader reads the file line by line, and for the files
    that are given to us first line is always meta data and we don't want
    that to be taken into clustering as well. Which is why we use the list
    from index 1 rather than 0.
    Since we have 2 columns, when converted into list/array it is 2D list.
    Here, index 0 in each line is x-coordinate, index 1 is the y-coordinate
    So we can refer to them data[line_number][x/y].
    '''


def draw(xCords, yCords, xLabel, yLabel, clusterLabel, pointerColor):
    plot.xlabel(xLabel)
    plot.ylabel(yLabel)
    plot.title("Initial Plot")
    plot.scatter(xCords, yCords, color=pointerColor, s=10, label=clusterLabel)
    plot.legend()


def kFinder():
    "This finds the apt K value from the given cluster using gap-statistics"
    return 0
    # TODO


def toXandY(unorderedData):
    "This method converts seperates x and y co-ordinates for plotting"
    orderedData = []
    orderedData.append([])        # Add a new sublsit every time
    orderedData.append([])        # Add a new sublsit every time
    listSize = len(unorderedData)
    for x in range(0, listSize):
            orderedData[0].append(unorderedData[x][0])  # Seperates the x-cords
    for y in range(0, listSize):
            orderedData[1].append(unorderedData[y][1])  # Seperates the y-cords
    return orderedData


cluster() # Executes the whole code above
plot.show() # Shows the graph that is drawn in memoery

'''
    Base Video : https://youtu.be/RD0nNK51Fp8
'''
