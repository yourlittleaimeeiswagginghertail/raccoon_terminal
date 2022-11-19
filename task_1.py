import numpy as np
from numpy import random
"""
#прямоугольник из нолей
truck = np.zeros( (3, 4), dtype = int)
print(truck)


#прямоугольник из единиц
truck2 = np.ones( (5, 6), dtype = int)
print(truck2)

lin = 5
col = 6

bike = np.random.randint(1, 10, size=(lin, col))
print(bike, "\n")

road = bike[1:(lin-1), 1:(col-1)]
print(road)
"""

text = input("enter 2 numbers: ")
cat = text.split(" ")
lin, col = map(int, cat)

#прямоугольник из единиц
truck2 = np.ones( (lin, col), dtype = int)
#print(truck2)

truck2[1:(lin-1), 1:(col-1)] = 0
print(truck2)
