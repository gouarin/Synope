from __future__ import print_function
import pySynope
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import mpl_toolkits.mplot3d as a3


c = pySynope.Sphere(1)
x, y, z = c.cloud_with_square(10)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(x, y, z, color='b')
ax.plot_wireframe(x, y, z, color='b')
plt.show()

c = pySynope.Superellipsoid(1, 1, 1, 1, 1)
x, y, z = c.cloud_with_square(10)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z, color='b')
plt.show()