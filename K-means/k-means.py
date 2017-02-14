# thou shall not cross 80 columns in thy file

import csv
import random
import math
import matplotlib.pyplot as plot


class Kmeans(object):
    "K-means clustering algorithm"

    def __init__(self, unclusteredData=[]):
        self.data = unclusteredData

    def cluster(self):
        "This is the main method, which executes k-means clustering algorithm"
        k = 3  # k is the number of clusters to be develped from the data
        for i in range(0,3):
            centriod[i] = random.choice(data)
            # These are the randomly picked centroids

    def parse():
        "Parses the data sets from the csv file we are given to work with"
        file = open("exercise-1.csv")  # should be manualized later
        rawFile = csv.reader(file)    # Reading the csv file into a raw form
        rawData = list(rawFile)       # Converting the raw data into list from.
        dataObject = Kmeans(rawData)  # Creating the obj and passing the data
        '''
        Remember, csv reader reads the file line by line, and for the files
        that are given to us first line is always meta data and we don't want
        that to be taken into clustering as well. Which is why we use the list
        from index 1 rather than 0.
        Since we have 2 columns, when converted into list/array it is 2D list.
        Here, index 0 in each line is x-coordinate, index 1 is the y-coordinate
        So we can refer to them data[line_number][x/y].
        We also need to convert them to a number.They are read as string
        '''

    def euclideanDistance(self, p, q):
        "This calculates the Euclidean Distance b/w p & q, in the standard way"
        distance = math.sqrt(((p[][0]-q[][0])**2) + ((p[][1]-p[][1])**2))
        return distance
    
    def draw(xCords, yCords, xLabel, yLabel, keyword, pointerColor="black"):
        # size = len(self.data)
        plot.xlabel(xLabel)
        plot.ylabel(yLabel)
        plot.title("Initial Plot")
        plot.legend()
        plot.scatter(xCords, yCords,label="mainGraph", color=pointerColor, s=10)
        if keyword == True:
            plot.show()

# inf
# https://youtu.be/RD0nNK51Fp8
