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
import numpy as np

quote = "If Socialism can only be realized when the intellectual development of all the people permits it, then we shall not see Socialism for at least five hundred years"

words = quote.split(" ")

#print(words)

selected = []

for onewo in words:
	#print(onewo)
	lecount = 0
	for letter in onewo:
		#print(letter)
		selected.append(letter)
		lecount += 1
		if lecount == 2:
			break
		else:
			nothing =  "nothing"

#print(selected)
result =  "".join(selected)
print(result, "\n")
print(quote)




