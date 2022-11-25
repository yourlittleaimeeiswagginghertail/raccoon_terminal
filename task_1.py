"""
import numpy as np



#**********************       [0, 1)     ***************
dog1 = np.random.rand(10)
dog1s = np.sort(dog1, axis=0)
dog1sr = np.around(dog1s, 2)
print(dog1sr)


truck = np.amax(dog1sr)
print(truck)

#np.amax(dog1sr) = 0
print(dog1sr)




#проверить копия меняется ли ориджинал




cat1 = np.array([-4.6, -1.2, -0.9, -0.2, 0, 1.2, 2.8])
print(cat1)


print("способ 1", cat1 - (cat1 % 1.0))

print("способ 2", np.floor(cat1))
"""





