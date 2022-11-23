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
