from Geom import *
import numpy as np

class Point(Geom):
    '''
    Documentation:
        Point Class

    Instructions:
        A point can be constructed:
            1) A = Point(5,7,1) # 5,7,1 correspond to the X,Y and Z coordinates
            2) A = Point(5,7) # 5,7 correspond to the X and Y coordinates. Z is treated as zero value
            2) A = Point([5,7,1]) # a list is used to construct the object. The list MUST contains 3 elements
    Errors:
        1) A = Point([5,7]) # the object cannot be constructed specifying only X and Y coordinates.
                ---- > A = Point([5,7,0]) is an alternative option
    Methods:
        class_name.coords  = returns the coordinates of the object in a list
        class_name.X = returns the X coordinate of the object
        class_name.Y = returns the Y coordinate of the object
        class_name.Z = returns the Z coordinate of the object
        class_name.getStartPoint = returns the coordinates of the point. [ class_name.getStartPoint = class_name.coords = class_name.getEndPoint ]
        class_name.getEndPoint = returns the coordinates of the point. [ class_name.getStartPoint = class_name.coords = class_name.getEndPoint ]
        class_name.addPoint = Point object cannot add another point

    Setter:
        The coordinates of an object can be changes using setters
        class_name.X = Value
        class_name.Y = Value
        class_name.Z = Value

        Example:
            A.X = 5
            A.Y = 7
            # Now, the X and Y coordinates of object A are 5 and 7.
    '''

    def __init__(self,X=0,Y=0,Z=0):
        # it tries to instantiate the object using the X,Y,Z coordinates
        try:
            # converts the input to floats. If the input datatype cannot be casted to float, then it tries to instantiate the object
            # supposing that the X inputs is a list.
            if isinstance(float(X),float) and isinstance(float(Y),float) and isinstance(float(Z),float):
                self.__coords = np.array([X,Y,Z]) # instantiate a coordinates matrix (np.ndarray) which is
                self.__coords.shape = (1,3) # defines the shape of __coords array
        except Exception:
            try:
                # checks if the X inputs is a list
                if isinstance(X,list):
                    if len(X) == 3: # checks if X has a length of 3
                        self.__coords = np.array([X])
                    elif len(X) == 2: # checks if X has a length of 2
                        self.__coords = np.array([X + [0]]) # the point is created setting the z coordinate equal of zero
            except Exception:
                print('[ The instance has not been instantiated correctly. Recosntruct it specifying X,Y and Z coordinates or a list containing the coordinates ]')


   # gets the projected coordinates concatenated
    @property
    def coords(self):
        # the function is enclosed in try/except block - If the object is not instantiated correctly, then the coordinates cannot be retrieved
        try:
            return self.__coords[0]
        except Exception:
            print('[ The instance has not been instantiated correctly. Recosntruct it specifying X,Y and Z coordinates or a list containing the coordinates ]')

    # gets the projected X,Y,Z coordinates separated
    @property
    def X(self):
        return self.coords[0] # X coordinate
    @property
    def Y(self):
        return self.coords[1] # Y coordinate
    @property
    def Z(self):
        return self.coords[2] # Z coordinate

    # sets the projected X,Y,Z coordinates separated
    @X.setter
    def X(self, X):
        self.coords[0] = X #  X coordinate setter
    @Y.setter
    def Y(self,Y):
        self.coords[1] = Y # Y coordinate setter
    @Z.setter
    def Z(self,Z):
        self.coords[2] = Z # Z coordinate setter

    # Override superclass methods
    # returns the coordinates of the Point's class object
    def getStartPoint(self):
        return self.coords
    # starting points = ending point
    def getEndPoint(self):
        return self.getStartPoint()
    # a point element cannot add another point
    def addPoint(self, point):
        print('Point Class cannot add another point.')