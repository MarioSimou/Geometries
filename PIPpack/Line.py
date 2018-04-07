from Geom import *
from Point import *
import numpy as np
import os
import math

class Line(Geom):
    '''
    Documentation:
        Line Class
    Instructions:
        A line can be constructed:
            CAUTION: The Line class is based to the Point class for its construction. ONLY Point class objects are acceptable

            # Specifying a list which contains all the Point's class objects
                Both examples below are threaded the same

            A = Line([Point1, Point2, Point3])
            A = Line([Point1.coords, Point2.coords, Point3.coords])

            # Reading a specified file
                The file reading is based on the method of numpy package, genfromtxt (see https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.genfromtxt.html)

            A = Line([]).createFeatureFromFile('filename')

    Methods:

        class.createFeatureFromFile(directory = 'filename', delim=',', header=1, type='float')

        # Instantiates the Line object specifying the directory of the file which will be read. The file must contains
        only X,Y and Z coordinates. If Z coordinates are not included, then, the coordinates will be populated with zeros.
        The method is based on genfromtxt method of numpy package. See (https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.genfromtxt.html)
        for further documentation

        class.getMBR()

        # Returns the minimum bounding rectangle of the object. No parameters are needed

        class.isIntersect(startPoint,endPoint,checkPoint)

        # Determines if the vector which is developed between a startPoint and endPoint, incorporates the location
        of checkpoint. The startPoint, endPoint and checkPoint elements they can be Point object, np.ndarrays or lists
        of coordinates,
        The method will threat accordingly all the parameters

        class.getOrientationAngle(point1,point2)

        # Determines the orientation of a point1 and point2. The orientation is calculated with an arbitrary north axes.
        The return angle is on gradians. Therefore for conversions:
            degrees : gradians * 180/200
            radians : gradians * PI /200
        The point1 and point2 elements they can be lists, Point objects or np.ndarrays.

        class.addPoint(point)
        # Adds a point to the object - The object must be a Point object or an np.ndArray

        Example:
        class.addPoint(Point(5,7).coords)
        class.addPoint(Point(5,7))

    '''
    def __init__(self, l = []):
        # __setArrayMat() = 'private' method within the object. It constructs the object specifying a list of Point objects
        self.__setArrayMat(l)

    # sets the getter method of returned coordinates
    @property
    def coords(self):
        return  self.__coords
    # setter of object's coordinates
    @coords.setter
    def coords(self, l):
        self.__setArrayMat(l)

    # private method which construct the matrix of coordinates everytime which is recalled
    def __setArrayMat(self, l = []):
        try:
            # checks if the elements of the list are part of np.ndarray class
            if all([isinstance(n, np.ndarray) for n in l]):
                self.__coords = np.array(map(np.vstack,l)).reshape(-1,3) # sets the coords array and define its dimensions
            elif all([isinstance(n, Point) for n in l]):
                l = [x.coords for x in l] # the list is reconstructed
                self.__coords = np.array(map(np.vstack, l)).reshape(-1, 3) # coordinates are set in a np.ndarray
        except Exception:
                print(' [ Read the documentation. The Line class in not instantiated ]')

    # read a file and constructs the current object using X,Y,Z coordinates of the file
    def createFeatureFromFile(self, directory, delim=',', header=1, type='float'):
        # reads a file with points using np.genfromtxt method
        try:
            points = np.genfromtxt(directory, delimiter=delim, skip_header=header, dtype=type)
        except Exception:
            print ('[ Error during file reading. Specify a validate directory. ]')
        # checks the dimensions of points np.ndarray
        # if the number of columns are 3, then is a 3D array which automatically is instantiate the object
        if points.shape[1] == 3:
            # checks if the points array contains nan values. If the array does not contain any nan values, then, the object will be constructed
            if not self.__isNan(points):
                self.__setArrayMat(points)
            # if the points array contains nan values, an exception will be thrown
            else:
                raise Exception('[ he 3D array contains nan values. Replace nan values with zeros, or populate the nan values with their correspond value. ]')
        # if the number of columns are 2, then a vector of zero elements is added in order to create a 3D array
        elif points.shape[1] == 2:
            # checks if the points array contains nan values. If the array does not contain any nan values, then, the object will be constructed
            if not self.__isNan(points):
                zeroV = np.zeros((points.shape[0], 1))  # creates a vector with zero elements
                self.__setArrayMat(np.hstack((points,zeroV)))  # concatenate together the points 2D array with the zeros vector and reconstruct the array
            # if the points array contains nan values, an exception will be thrown
            else:
                raise Exception('[ The 2D array contains nan values. Replace nan values with zeros, or populate the nan values with their correspond value. ]')
        else:
            raise Exception('[ Non 2D or 3D specified array in the file. The file that is specified need to contains X,Y or X,Y,Z coordinates ]')
        return self


    # 'private' method which is used during the object construction. Identifies if an imported array contains nan values
    def __isNan(self, points):
        return (any([any(k) for k in [[np.isnan(j) for j in i] for i in points]]))

    def addPoint(self, point):
        try:
            if isinstance(point,np.ndarray): # check if the point is an np.ndarray
                if len(point) == 3:
                    # checks the size of the point object
                    self.coords = np.vstack((self.coords,point))
            elif isinstance(point,Point):
                self.coords = np.vstack((self.coords, point.coords))
            else:
                raise Exception('[ The size of the point parameter does not capture a pair of X,Y,Z coordinates ]')
        except Exception:
            print('[The point is not added]')

    # determines the Minimum Bounding Box of the object.
    def getMBR(self):
        # identify the x and y coordinates
        xmin = min(self.getXVector()) # min x coordinate
        xmax = max(self.getXVector()) # max x coordinate
        ymin = min(self.getYVector()) # min y coordinate
        ymax = max(self.getYVector()) # max y coordinate
                # tuples packing
        return ((xmin,ymin), (xmax,ymax)) # the lower and upper edge of the MBR are returned

    # determines if the checkpoint lies within the vector of starting and ending point
    def isIntersect(self, startPoint,endPoint,checkPoint):
        # sets an initial condition
        intersect = False
        # if the azimuth of checkpoint and the azimuth of the vector that is created using the startPoint and endPoint
        # are equal, then the checkPoint is located along the vector
        if (isinstance(startPoint,Point) or isinstance(startPoint,np.ndarray) or isinstance(startPoint,list))and (isinstance(endPoint,Point) or isinstance(endPoint,np.ndarray) or isinstance(endPoint,list)) and (isinstance(checkPoint,Point) or isinstance(checkPoint,np.ndarray) or isinstance(checkPoint,list)) :
            if self.getOrientationAngle(startPoint,endPoint) == self.getOrientationAngle(startPoint,checkPoint):
                intersect = True
        else:
            raise Exception('[ The points are not instances of Point Class. Create the points elements and try again. ]')
        return intersect

    # determines the orientation angle between two points.
    def getOrientationAngle(self, point1,point2):
            # checks if the point1 and point2 objects are instances of Point class
            if isinstance(point1,Point) and isinstance(point2,Point):
                dx = point2.X - point1.X # x coordinates
                dy = point2.Y - point1.Y # y coordinates
            # checks if the point1 and point2 objects' data type is 3D/2D lists or nd.ndarrays
            elif (isinstance(point1,np.ndarray) or isinstance(point1,list)) and (isinstance(point2,np.ndarray) or isinstance(point2,list)):
                if (len(point1) == 3 or len(point1) == 2) and  (len(point2) == 3 or len(point2) == 2): # checks if the imported points are 2D or 3D
                    dx = point2[0] - point1[0] # x coordinates
                    dy = point2[1] - point1[1] # y coordinates
            else:
                raise Exception('[ The points are not instances of Point Class or np.ndArray format. Read the documentation.]')

            PI =math.pi # PI = 3.1415926535...

            # conditions in order to set the orientation
            # the angle is return in gradians
            if dx > 0 and dy > 0:
                angle = math.atan((dx/dy)) * (200/PI)
            elif dx > 0 and dy < 0:
                angle = 200 + math.atan((dx/dy)) * (200/PI)
            elif dx < 0 and dy < 0:
                angle = 200 + math.atan((dx/dy)) * (200/PI)
            elif dx < 0 and dy > 0:
                angle = 400 - math.atan((dx/dy)) * (200/PI)
            elif dx == 0 and dy >=0:
                angle = 0
            elif dx == 0 and dy < 0:
                angle = 200
            elif dx > 0 and dy == 0:
                angle = 100
            elif dx <0 and dy == 0:
                angle = 300
            return angle  # return the angle between the imported points
