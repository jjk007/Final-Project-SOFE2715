import matplotlib.pyplot as plt

dates = [0, 1, 2, 3, 4, 5]
dates1 = [2, 4, 5, 6, 4, 1]
values = [2, 1, 1, 1, 1, 2]
values1 = [3, 4, 7, 4, 2, 9]

plt.scatter(dates1, values1)
plt.plot(dates, values, '-o')
plt.show()
