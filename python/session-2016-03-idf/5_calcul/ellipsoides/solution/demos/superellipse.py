from __future__ import print_function
import pySynope
import matplotlib.pyplot as plt

c = pySynope.Circle(1)
x, y = c.cloud_with_square(10)
plt.plot(x, y, '.')
plt.show()

c = pySynope.Superellipse(1, 1, 100)
x, y = c.cloud(100)
plt.plot(x, y, '.')
plt.show()