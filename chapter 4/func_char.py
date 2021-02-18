import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return (3-0.1*x)/(1-x)


X = np.linspace(-10,10,20)
Y = func(X)

plt.plot(X,Y,"g")
plt.show()
