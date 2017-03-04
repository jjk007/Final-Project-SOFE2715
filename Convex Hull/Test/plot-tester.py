import matplotlib.pyplot as plt

x = [1, 3, 7, 6, 2, 1]
y = [1, 0, 3, 7, 5, 1]

x1 = [2, 4, 6, 4, 3, 5]
y1 = [3, 4, 4, 2, 1, 4]

plt.plot(x, y, '-o')  # Make the boundaries
plt.scatter(x1, y1, marker=(5, 2), color="r")
plt.show()
