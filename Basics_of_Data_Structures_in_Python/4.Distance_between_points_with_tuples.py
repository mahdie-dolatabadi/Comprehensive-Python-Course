# variable definitions
a = (3, 4)
b = (0, 0)
coordinates = (a, b)

# calculating the distance
distance = (((coordinates[0][0] - coordinates[1][0]) ** 2) + ((coordinates[0][1] - coordinates[1][1]) ** 2)) ** 0.5


print(distance)