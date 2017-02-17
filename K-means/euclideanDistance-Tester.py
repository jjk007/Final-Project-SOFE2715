import math



def euclideanDistance(p=0, q=0):
    p=float(2.35400000000)
    "This calculates the Euclidean Distance b/w p & q, in the standard way"
    distance = math.sqrt(((p-54.6)**2) + ((5454-0.2154)**2))
    return distance

print euclideanDistance()
