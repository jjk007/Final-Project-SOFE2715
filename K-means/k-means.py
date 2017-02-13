import csv
import random
import math
import matplotlib.pyplot as plt


class Kmeans(object):
    "K-means clustering algorithm"

    def __init__(self, unclusteredData=[]):
        self.data = unclusteredData

    def cluster(self):
        "This is the main method, which executes k-means clustering algorithm"
        k = 5  # k is the number of clusters to be develped from the data
        c1 = random.choice(data)# These are the randomly picked centroids
        c2 = random.choice(data)# Data is the list of unclustered data we've got
        c3 = random.choice(data)
        c4 = random.choice(data)
        c5 = random.choice(data)

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

    def draw(self, xCords, yCords, pointerColor="k"):
        # size = len(self.data)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Initial Plot")
        plt.legend()
        plt.show()
        plt.scatter(xCords, yCords, label="Graph1", color=pointerColor, s=10)
        # TODO

# inf
# https://youtu.be/RD0nNK51Fp8
