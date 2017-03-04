#!/usr/bin/env python2.7
# thou shall not cross 80 columns in thy file

from timeit import default_timer as timer
import math
import matplotlib.pyplot as plot
import csv

newData = []


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


def euclideanDistance(p, q):
    "This calculates the Euclidean Distance b/w p & q, in the standard way"
    distance = math.sqrt(((p[0]-q[0])**2) + ((p[1]-q[1])**2))
    return distance


def locate_min(a):
    smallest = min(a)  # Locating all minmum elements of the passed list
    return [index for index, element in enumerate(a)
            if smallest == element]


def parse():
    "Parses the data sets from the csv file we are given to work with"
    file = open("./Exercises/exercise-6.csv")  # should be manualized later
    rawFile = csv.reader(file)    # Reading the csv file into a raw form
    rawData = list(rawFile)       # Converting the raw data into list from.
    return rawData


def main():
    global newData
    start = timer()
    data = parse()                  # Calling the parse funtion we made
    labels = data.pop(0)
    listSize = len(data)
    for i in range(0, listSize):    # Converting the string list to float
        newData.append([])          # Add a new sublsit every time
        for j in range(0, 2):       # Append converted data to the new list
            newData[i].append(float(data[i][j]))
    # Finding the starting point P
    tempData = toXandY(newData)  # tempData -> [[Xs][Ys]]
    P = tempData[1].index(min(tempData[1]))  # Locating the minimum y-cord

    # Timer
    end = timer()
    print "Amount of time elapsed to service " + labels[0] + " and " + labels[1] + " : " + str(end-start) + " seconds"


if __name__ == "__main__":
    main()
