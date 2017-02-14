import csv


def parse():
        "Parses the data sets from the csv file we are given to work with"
        file = open("exercise-4.csv")  # should be manualized later
        rawFile = csv.reader(file)    # Reading the csv file into a raw form
        rawData = list(rawFile)       # Converting the raw data into list from.
        # dataObject = Kmeans(rawData)  # Creating the obj and passing the data
        for val in rawData:
            print (val)


parse()
