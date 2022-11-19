import numpy as np
from numpy import random



#куб 3 на 3 на 3
bike = random.randint(10, 20, size=(3, 3, 3))
print(bike)

#наименьш из array
roof = np.amin(bike)
print(roof)

#макс из array
building = np.amax(bike)
print(building)

