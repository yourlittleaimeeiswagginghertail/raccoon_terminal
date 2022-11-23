"""
import pylab

x = pylab.linspace(-6, 6, 1000)

def gaussian(x, sigma):
    #Return the normalized Gaussian with standard deviation sigma
    c = pylab.sqrt(2 * pylab.pi)
    return pylab.exp(-0.5 * (x / sigma)**2) / sigma / c

sigma1 = 1
g1 = gaussian(x, sigma1)

pylab.plot(x, g1)

pylab.show()

"""

"""
import pylab
x = 3
sigma = 5

def gaus(x, sigma):
    return round(1/(sigma*pylab.sqrt(2*pylab.pi))*pylab.exp(-1*x**2/(2*sigma**2)), 5)


print(gaus(x, sigma))

"""
"""
import numpy as np

bone = np.random.normal(loc=10,  scale=5, size=(20, 1))
print(bone, "\n")

skeleton = np.sort(bone, axis=0)
print(skeleton)

#skeleton = np.sort(coffin, axis=0)
#print(skeleton, "\n")

"""
import numpy as np

for repeat in range(1):
	mu1 = float(5)
	sigma1 = float(2)
	amo_num = int(100)

	bone1 = np.random.normal(loc=mu1,scale=sigma1,size=(amo_num))
	bone2 = np.around(bone1, 3)
	bone3 = np.sort(bone2, axis=0)
	print("numbers: ", bone3, "\n")
	
"""
	mu2 = np.average(bone3)
	print("*****"*6, round(mu2, 3))

	sigma2 = np.std(bone3)
	print("*****"*6, round(sigma2, 3), "\n")
"""


coffin = bone3[ ( bone3>=(mu1-sigma1) ) & ( bone3<=(mu1+sigma1) ) ]
print("отличаются от среднего не более чем на одну сигму:", coffin)
























