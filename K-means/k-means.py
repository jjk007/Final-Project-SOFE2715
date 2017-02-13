import csv
import random
import matplotlib

class Kmeans(object):
    "K-means clustering algorithm"

    def __init__(self, unclusteredData=[]):
        self.data = unclusteredData

    def cluster(self):
        "This is the main method, which executes k-means clustering algorithm"
        k = 5 # k is the number of clusters to be develped from the data
        c1 = random.choice(data)# These are the randomly picked centroids
        c2 = random.choice(data)# data is the list of unclustered data we've got
        c3 = random.choice(data)
        c4 = random.choice(data)
        c5 = random.choice(data)

        abc = 1+1
        print abc
        return 0

    def parse(self):
        "Parses the data sets from the csv file we are given to work with"
        # TODO
        return 0

    def euclideanDistance(self, xCord, yCord):
        "This calculates the Euclidean Distance b/w X & Y, in the standard way"
        distance = xCord + yCord
        # TODO
        return distance

    def display(self):
        "Displays the data, for TESTING"
        #TODO
        return 0


# inf
# https://youtu.be/RD0nNK51Fp8
