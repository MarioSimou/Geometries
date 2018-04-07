import numpy as np
import matplotlib.pyplot as py

class Geom(object):
    '''
    Documentation:
        CAUTION : Geom class cannot be instantiated

    Methods:
        .getStartPoint()
        # Returns the starting point of the object

        .getEndPoint()
        # Returns the ending point of the object

        .getNumPoint()
        # Returns the number of points that are contained in the object

        .addPoint(point)
        # Adds a point to the object - The object must be a Point object or an np.ndArray

        Example:
        class.addPoint(Point(5,7).coords)

        .getXYVector()
        # returns the X and Y coordinates of the object in tuple data type

        .getXVector()
        # returns the vector of X coordinates of the object

        .getYVector()
        # returns the vector of Y coordinates of the object

        .plotPoints()
        # plots the points of the object
    '''

    def getStartPoint(self):
        return self.coords[0]

    def getEndPoint(self):
        return self.coords[-1]
    def addPoint(self, point):
        try:
            if isinstance(point,np.ndarray): # check if the point is an np.ndarray
                if len(point) == 3:
                    # checks the size of the point object
                    self.coords = np.vstack((self.coords,point))
            else:
                raise Exception('[ The size of the point parameter does not capture a pair of X,Y,Z coordinates ]')
        except Exception:
            print('[The point is not added]')

    def getNumPoints(self):
        if len(self.coords.shape) ==  2:
            return self.coords.shape[0] # for lines and polygons
        else:
            return 1 # for points

    # returns the X and Y coordinates of the object in a tuple - It needs to be unpacked
    def getXYVector(self):
        # pack and sorting
        pack = sorted(zip([k[0] for k in [[j for j in i] for i in self.coords]], [k[1] for k in [[j for j in i] for i in self.coords]])) # sorted
        # x and y coordinates
        x = []
        y = []
        for xs,ys in pack:
            x.append(xs)
            y.append(ys)

        return (x,y)

    # retuns the vector of X coordinates
    def getXVector(self):
        return [k[0] for k in [[j for j in i] for i in self.coords]]
    # retuns the vector of Y coordinates
    def getYVector(self):
        return [k[1] for k in [[j for j in i] for i in self.coords]]
    # plots the points of object
    def plotPoints(self):
        x = self.getXVector()  # x coordinates
        y = self.getYVector()  # y coordinates    py.plot(x,y, 'rs') # set the style of the points
        py.xlabel('X-Coordinates') # set X axes
        py.ylabel('Y-Coordinates') # set Y axes
        py.axis([min(x)-2,max(x)+2,min(y)-2,max(y)+2]) # sets the extent of the plot
        py.show() # shows the plot

