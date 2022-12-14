###Three-dimensional plotting using matplotlib
"""
There are many options for doing 3D plots in Python, but here are some common and easy ways using Matplotlib.

In general, the first step is to create a 3D axes, and then plot any of the 3D graphs that best illustrates the data for a particular need. In order to use Matplotlib, the mplot3d toolkit that is included with the Matplotlib installation has to be imported:
"""

from mpl_toolkits import mplot3d

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

"""It is inside this 3D axes that a plot can be drawn, it is important to know what type of plot (or combination of plots) will be better to describe the data.

At this point in time, you need to note that this comprises our base for further plotting.

###Points and Lines:

The following image combines 2 plots, one with a line that goes through every point of the data, and others that draw a point on each of the particular 1000 values on this example.

The code is actually very simple when you try to analyze it. We have made use of standard trigonometric functions to plot a set of random values to obtain our projection in 3 dimensions.
"""

ax = plt.axes(projection='3d')# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

"""###3D Contour Plots:

The input for the contour plot is a bit different than for the previous plot, as it needs the data on a two-dimensional grid.

Note that on the following example that after assigning values for x and y, they are combined on a grid by executing “np.meshgrid(x, y)” and then the Z values are created from executing the function f(X,Y) with the values of the grid (Z=f(X,Y)).

Again, basic 3d plot simplified in the following code:
"""

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

"""On the previous graphs, the data was generated in order, but in real life sometimes the data is not ordered, for those cases, surface triangulation is very useful as it creates surfaces by finding sets of triangles formed between adjacent points.

###Surface Triangulation
"""

theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)
ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z,cmap='viridis', edgecolor='none')