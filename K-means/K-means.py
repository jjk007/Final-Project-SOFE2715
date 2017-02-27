# thou shall not cross 80 columns in thy file

import csv
import random
import time
from timeit import default_timer as timer
import math
import matplotlib.pyplot as plot


centroid = list()            # Stores the random centriods, we generate
calculatedCentroid = list()  # Stores the calculated centroids
clustered = list()           # Stores the clustered data in orderered form
newData = []                 # Stores the type converted data in float
K = 0                       # K is the number of clusters
count = 0


def cluster():
    "This function performs the k-means clustering algorithm"
    global count
    global centroid
    global calculatedCentroid
    global clustered
    global K
    distance = [0]*K
    del clustered[:]  # Empty the old cluster before appending new
    for i in range(K):
        clustered.append([])  # Making a sublist for every cluster

    for val in newData:
        for i in range(0, K):
            distance[i] = euclideanDistance(centroid[i], val)
            # Only this statement should be in the inner loop
            '''
            Here I am calculating the distance between centroid & each
            value to classify them into differnt clusters
            '''
        minIndex = distance.index(min(distance))  # Both of these should be
        clustered[minIndex].append(val)           # should be in the outer loop

    del calculatedCentroid[:]  # Empty the calculatedCentroid list everytime
    for i in range(0, K):      # Calculate new centriods
        calculatedCentroid.append(meanCords(clustered[i]))

    if cmp(calculatedCentroid, centroid) == 0:  # Comapre old and new centriods
        return count

    centroid = list(calculatedCentroid)  # Copying new centriod to the old var
    count += 1
    cluster()  # Recursively calling cluster() again and again


def euclideanDistance(p, q):
    "This calculates the Euclidean Distance b/w p & q, in the standard way"
    distance = math.sqrt(((p[0]-q[0])**2) + ((p[1]-q[1])**2))
    return distance


def parse():
    "Parses the data sets from the csv file we are given to work with"
    file = open("./Exercises/exercise-2.csv")  # should be manualized later
    rawFile = csv.reader(file)    # Reading the csv file into a raw form
    rawData = list(rawFile)       # Converting the raw data into list from.
    return rawData
    '''
    Csv reader reads the file line by line, and for the files
    that are given to us first line is always meta data and we don't want
    that to be taken into clustering as well. Which is why we use the list
    from index 1 rather than 0.
    Since we have 2 columns, when converted into list/array it is 2D list.
    Here, index 0 in each line is x-coordinate, index 1 is the y-coordinate
    '''


def draw(xCords, yCords, xLabel, yLabel, clusterLabel, pointerColor):
    "This method draws the clusterd plot using Matplotlib"
    plot.xlabel(xLabel)
    plot.ylabel(yLabel)
    plot.title("Initial Plot")
    plot.scatter(xCords, yCords, color=pointerColor, s=10, label=clusterLabel)
    plot.legend()


def kFinder():
    "This finds the apt K value from the given cluster using gap-statistics"
    return 4
    # return random.randint(2, 5)
    # TODO


def meanCords(unorderedCluster):
    "This finds the mean of the clusters to reassign the centroids"
    orderedCluster = toXandY(unorderedCluster)
    listSize = len(orderedCluster[0])
    totalX = 0
    totalY = 0
    for i in range(0, listSize):
        totalX += orderedCluster[0][i] # Adds up all the X-cords
    for i in range(0, listSize):
        totalY += orderedCluster[1][i] # Adds up all the Y-cords
    avgX = totalX/listSize
    avgY = totalY/listSize
    newCentroids = [0,0]
    newCentroids[0] = avgX
    newCentroids[1] = avgY
    return newCentroids  # Return the mean of the x or y co-ordinates


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


def main():
    "This is the main method were execusion begins"
    global K
    global count
    start = timer()
    K = kFinder()
    names = ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]
    color = ["r", "g", "b", "m", "c"]  # Stores the color values
    data = parse()                     # Calling the parse funtion we made
    labels = data.pop(0)
    listSize = len(data)
    for i in range(0, listSize):    # Converting the string list to float
        newData.append([])          # Add a new sublsit every time
        for j in range(0, 2):       # Append converted data to the new list
            newData[i].append(float(data[i][j]))
    # These are the randomly picked centroids, should be re-calculated later
    for i in range(0, K):
        centroid.append(random.choice(newData))
    cluster()  # Executes the algorithm
    end = timer()
    print "Number of iterations: " + str(count)
    print "Amount of time elapsed: " + str(end-start)+ " seconds"
    # Now we plot them
    for i in range(0, K):
        clustered[i] = toXandY(clustered[i])  # Seperates X and Y cords
        draw(clustered[i][0], clustered[i][1],
             labels[0], labels[1], names[i], color[i])
    plot.show()  # Shows the graph that is drawn in memory

if __name__ == "__main__":
    main()
