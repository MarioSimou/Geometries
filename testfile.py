from PIPpack import *
import numpy as np
import os

# Set Directory
directory = os.path.join(os.getcwd(),'Points')
os.chdir(directory)

# Points Reading
pointsFile = np.genfromtxt(os.path.join(directory,'testPoints.csv'), delimiter=',', skip_header=1)
print(pointsFile)

# File Reading and Polygon Creation
poly = Polygon([]).createFeatureFromFile(os.path.join(directory,'testPoly.csv'))
pA = Point([19,7.0])

# print the starting point
print('Starting point: %s' %(poly.getStartPoint()))
# print the ending point
print('Ending point: %s' %(poly.getEndPoint()))
# show the MBR
print('MBR: %s %s ' %(poly.getMBR()))
# show the number of points
print('Number of points: %s' %(poly.getNumPoints()))
# add a point
print('Coordinates before point addition\n %s' %(poly.coords))
print (Point(3,5).coords)
poly.addPoint(Point(3,5))
print('Coordinates after point addition\n %s' %(poly.coords))

for i in pointsFile:
    print(i)
# Test whether the point is inside the polygon
    print(poly.contains(i))
    # Plot Content
    poly.plotPoints(i)

