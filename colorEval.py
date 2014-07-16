import scipy.optimize as optimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from pylab import *
import numpy as np
from matplotlib import cm
from refcolors import *
from color import *

fig = plt.figure()
ax = fig.gca(projection='3d')

X,Y,Z = [],[],[]

for x in range(len(baseColors)):
  for y in range(len(colorSets[x])):
    setC = color(colorSets[x][y]).hsv("h")
    if setC > 180:
      setC -= 360
    X += [ color(colorSets[x][y]).hsv("h") ]

    Y += [ enumeration[y]  ]
    
    specC = color(baseColors[x]).hsv("h")
    if specC > 180:
      specC -= 360
    Z += [ specC - setC ]
p = ax.scatter(X,Y,Z,c="r")
plt.show()

A = np.array(zip(X, Y, Z))

def func(data, a, b, c, d, e, f, g, h):
    return  a*data[:,0]**3 +\
            b*data[:,1]**3 +\
            c*data[:,0]**2 +\
            d*data[:,1]**2 +\
            e*data[:,0]*data[:,1] +\
            f*data[:,0] +\
            g*data[:,1] +\
            h

guess = (1,1,1,1,1,1,1,1)
params, pcov = optimize.curve_fit(func, A[:,:2], A[:,2], guess)
print "Hue"
print(params)

# # -------------------------------------

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# X,Y,Z = [],[],[]
# for x in range(len(baseColors)):
#   for y in range(len(colorSets[x])):
#     X += [ color(colorSets[x][y]).hsv("h") ]
#     Y += [ enumeration[y]  ]
#     Z += [ color(baseColors[x]).hsv("s") ]
# p = ax.scatter(X,Y,Z,c="g")
# plt.show()

# A = np.array(zip(X, Y, Z))

# def func(data, a, b, c, d, e, f, g, h):
#     return  a*data[:,0]**3 +\
#             b*data[:,1]**3 +\
#             c*data[:,0]**2 +\
#             d*data[:,1]**2 +\
#             e*data[:,0]*data[:,1] +\
#             f*data[:,0] +\
#             g*data[:,1] +\
#             h

# guess = (1,1,1,1,1,1,1,1)
# params, pcov = optimize.curve_fit(func, A[:,:2], A[:,2], guess)
# print "Sat"
# print(params)

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# X,Y,Z = [],[],[]
# for x in range(len(baseColors)):
#   # print colorSets[x]
#   for y in range(len(colorSets[x])):
#     X += [ color(colorSets[x][y]).hsv("h") ]
#     Y += [ enumeration[y]  ]
#     Z += [ color(baseColors[x]).hsv("v") ]
# p = ax.scatter(X,Y,Z,c="b")
# plt.show()

# A = np.array(zip(X, Y, Z))

# def func(data, a, b, c, d, e, f, g, h):
#     return  a*data[:,0]**3 +\
#             b*data[:,1]**3 +\
#             c*data[:,0]**2 +\
#             d*data[:,1]**2 +\
#             e*data[:,0]*data[:,1] +\
#             f*data[:,0] +\
#             g*data[:,1] +\
#             h

# guess = (1,1,1,1,1,1,1,1)
# params, pcov = optimize.curve_fit(func, A[:,:2], A[:,2], guess)
# print "Val"
# print(params)

hue = linspace(0,360)
grd = linspace(50,900)