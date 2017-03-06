#!/usr/bin/env python2.7
# thou shall not cross 80 columns in thy file

# Concex-Hull creation using Graham Scan Algorithm

from timeit import default_timer as timer
import csv
import math
import matplotlib.pyplot as plt


def scan(data):
    "This method generates the convex hull using Graham scan algorithm"
    hull = []            # Used like a stack here
    hull.append([])      # For the X-coordinates
    hull.append([])      # For the Y-coordinates
    return hull, data


def leftOrRight(p1, p2, p3):
    "Used to determine the right path for the convex points"
    cal1 = (p2[0] - p1[0]) * (p3[1] - p1[1])
    cal2 = (p2[1] - p1[1]) * (p3[0] - p1[0])
    diff = cal1 - cal2
    return diff


def sortI(base, data):
    '''
    This method sorts the array using insertion sort, the sort is special
    because it sorts the data based on the given base, not the data itself.
    Here it sorts the data based on the slope array passed as the base
     '''
    print "\nSorting started"
    size = len(base)
    for i in range(1, size):
        CurrentItem = base[i]
        # j is the divider of the sorted and unsorted portion
        j = i-1
        while j >= 0 and base[j] > CurrentItem:
            base[j+1] = base[j]  # Swap base array
            swap(data, j+1, j)   # Swap data array
            j = j-1  # incrementing the divider because we swapped values
            base[j+1] = CurrentItem
    return data  # Method ends here


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


def euclideanDistance(p, q):
    "This calculates the Euclidean Distance b/w p & q, in the standard way"
    distance = math.sqrt(((p[0]-q[0])**2) + ((p[1]-q[1])**2))
    return distance


def slope(data, P=0):
    "Calculates slopes between data-points and P"
    m = []
    m.append(0) # Dummy value for Pth Value slope
    listSize = len(data[0])
    for i in range(1, listSize): #Starting from 1 excluding P point
        m.append((data[1][i] - data[1][P])/(data[0][i] - data[0][P]))
    return m # Return the list with slopes


def draw(xCords, yCords, xLabel, yLabel, what):
    "This method draws the Convex-Hull plot using Matplotlib"
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title("Convex-Hull")
    if what == 1:
        plt.scatter(xCords, yCords, color="g", s=20)
    else:
        plt.plot(xCords, yCords, '-o', color="r")  # Make the boundaries
    # plt.legend()

def swap(data, i, j):
    "This method swaps the two points i and j in the list data"
    data[0][i], data[0][j] = data[0][j], data[0][i]  # Swap x-Cords
    data[1][i], data[1][j] = data[1][j], data[1][i]  # Swap y-cords
    return data

def parse():
    "Parses the data sets from the csv file we are given to work with"
    file = open("./Exercises/exercise-2.csv")  # should be manualized later
    rawFile = csv.reader(file)    # Reading the csv file into a raw form
    rawData = list(rawFile)       # Converting the raw data into list from.
    return rawData


def main():
    newData = []
    start = timer()
    data = parse()                  # Calling the parse funtion we made
    labels = data.pop(0)            # Necessary evil
    listSize = len(data)
    for i in range(0, listSize):    # Converting the string list to float
        newData.append([])          # Add a new sublsit every time
        for j in range(0, 2):       # Append converted data to the new list
            newData[i].append(float(data[i][j]))
    # Finding the starting point P
    DataXandY = toXandY(newData)     # DataXandY -> [[Xs][Ys]]
    P = DataXandY[1].index(min(DataXandY[1]))  # Locating the minimum y-cord
    DataXandY = swap(DataXandY, 0, P)
    P = 0                            # Because it was swapped
    slopes = slope(DataXandY, P)
    DataXandY = sortI(slopes, DataXandY)  # Sort the points ccw

    hull, DataXandY = scan(DataXandY)   # Call the graham scan algorithm

    end = timer()
    draw(DataXandY[0], DataXandY[1], labels[0], labels[1], 2)
    plt.show()
    print "Time elapsed: " + str(end-start) + " seconds" # Fix timer placement!


if __name__ == "__main__":
    main()
