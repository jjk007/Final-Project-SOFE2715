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
