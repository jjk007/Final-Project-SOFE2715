# thou shall not cross 80 columns in thy file

import csv
import random
import math
import matplotlib.pyplot as plot


centriod = list()
clusteredData = list()


def cluster():
    "This is the main method, which executes k-means clustering algorithm"
    k = 3  # k is the number of clusters to be develped from the data
    newData = []
    data = parse()
    labels = data.pop(0)
    listSize = len(data)
    clusteredData.append([])
    clusteredData.append([])
    clusteredData.append([])

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
            clusteredData[0].append(val)
        elif(distance2 > distance1 and distance2 > distance3):
            clusteredData[1].append(val)
        else:
            clusteredData[2].append(val)

    clusteredData[0] = toXandY(clusteredData[0]) 
    clusteredData[1] = toXandY(clusteredData[1]) 
    clusteredData[2] = toXandY(clusteredData[2]) 
    draw(clusteredData[0][0],clusteredData[0][1],labels[0],labels[1],"Cluster 1", False,"r")
    draw(clusteredData[1][0],clusteredData[1][1],labels[0],labels[1],"Cluster 2", False,"g")
    draw(clusteredData[2][0],clusteredData[2][1],labels[0],labels[1],"Cluster 3", True,"b")


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


def draw(xCords, yCords, xLabel, yLabel, clusterLabel, keyword, pointerColor):
    # size = len(self.data)
    plot.xlabel(xLabel)
    plot.ylabel(yLabel)
    plot.title("Initial Plot")
    plot.legend()
    plot.scatter(xCords, yCords, label=clusterLabel, color=pointerColor, s=10)
    if keyword:
        plot.show()


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

'''
    Base Video : https://youtu.be/RD0nNK51Fp8
'''
