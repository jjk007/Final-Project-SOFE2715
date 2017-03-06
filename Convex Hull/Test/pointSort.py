#!/usr/bin/env python2.7
# thou shall not cross 80 columns in thy file

# Concex-Hull creation using Graham Scan Algorithm

from timeit import default_timer as timer
import csv
import math
import matplotlib.pyplot as plt


def pointSort(data, P=17):
    "This method sorts the array using insertion sort"
    print "\nSorting started"
    size = len(data)
    for i in range(0, size):
        CurrentItem = data[i]
        # j is the divider of the sorted and unsorted portion
        j = i-1
        while j >= 0 and data[j] > CurrentItem:
            data[j+1] = data[j]  # Swap happens here.
            j = j-1  # incrementing the divider because we swapped values
            data[j+1] = CurrentItem
    return data  # Method ends here


def swap(data, i, j):
    "This method swaps the two points i and j in the list data"
    data[0][i], data[0][j] = data[0][j], data[0][i]  # Swap x-Cords
    data[1][i], data[1][j] = data[1][j], data[1][i]  # Swap y-cords




def parse():
    "Parses the data sets from the csv file we are given to work with"
    file = open("./Exercises/exercise-2.csv")  # should be manualized later
    rawFile = csv.reader(file)    # Reading the csv file into a raw form
    rawData = list(rawFile)       # Converting the raw data into list from.
    return rawData


def toXandY(unorderedData):
    "This method converts seperates x and y co-ordinates for plotting"
    orderedData = []
    orderedData.append([])        # Add a new sublist every time
    orderedData.append([])        # Add a new sublist every time
    listSize = len(unorderedData)
    for x in range(0, listSize):
        orderedData[0].append(unorderedData[x][0])  # Seperates the x-cords
    for y in range(0, listSize):
        orderedData[1].append(unorderedData[y][1])  # Seperates the y-cords
    return orderedData


