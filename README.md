Geometries repository
------------------------------------------------


Geom Class
----------------

         Methods
        # Returns the starting point of the object
        .getStartPoint()

        # Returns the ending point of the object
        .getEndPoint()
        
        # Returns the number of points that are contained in the object
        .getNumPoint()

        # Adds a point to the object - The object must be a Point object or an np.ndArray
        .addPoint(point)
         e.g class.addPoint(Point(5,7).coords)
        
        # returns the X and Y coordinates of the object in tuple data type
        .getXYVector()

        # returns the vector of X coordinates of the object
        .getXVector()
         
         # returns the vector of X coordinates of the object
        .getYVector()
                
        # plots the points of the object
        .plotPoints()
        
        
        
Point Class
---------------------

A point can be constructed:

> A = Point(5,7,1) # 5,7,1 correspond to the X,Y and Z coordinates

> A = Point(5,7) # 5,7 correspond to the X and Y coordinates. Z is treated as zero value

> A = Point([5,7,1]) # a list is used to construct the object. The list MUST contains 3 elements
    
        Methods:
        >class_name.coords  = returns the coordinates of the object in a list
        
        >class_name.X = returns the X coordinate of the object
        
        >class_name.Y = returns the Y coordinate of the object
        
        >class_name.Z = returns the Z coordinate of the object
        
        >class_name.getStartPoint = returns the coordinates of the point. [ class_name.getStartPoint = class_name.coords =                               class_name.getEndPoint ]
        
        >class_name.getEndPoint = returns the coordinates of the point. [ class_name.getStartPoint = class_name.coords =                                 class_name.getEndPoint ]
        
        >class_name.addPoint = Point object cannot add another point
    

Line Class
------------------------------------------

A line can be constructed:
__CAUTION: The Line class is based to the Point class for its construction. ONLY Point class objects are acceptable__

>A = Line([Point1, Point2, Point3])
>A = Line([Point1.coords, Point2.coords, Point3.coords])

__Reading a specified file__
>A = Line([]).createFeatureFromFile('filename', directory = 'filename', delim=',', header=1, type='float')
         
         Methods:

        # Instantiates the Line object specifying the directory of the file which will be read. The file must contains
        only X,Y and Z coordinates. If Z coordinates are not included, then, the coordinates will be populated with zeros.
        The method is based on genfromtxt method of numpy package. 
        >class.getMBR()
        
        # Returns the minimum bounding rectangle of the object. No parameters are needed
        >class.isIntersect(startPoint,endPoint,checkPoint)
        
        # Determines if the vector which is developed between a startPoint and endPoint, incorporates the location
        of checkpoint. The startPoint, endPoint and checkPoint elements they can be Point object, np.ndarrays or lists
        of coordinates,
        The method will threat accordingly all the parameters
        >class.getOrientationAngle(point1,point2)
        
        # Determines the orientation of a point1 and point2. The orientation is calculated with an arbitrary north axes.
        The return angle is on gradians. Therefore for conversions:
            degrees : gradians * 180/200
            radians : gradians * PI /200
        The point1 and point2 elements they can be lists, Point objects or np.ndarrays.
        >class.addPoint(point)
        
        # Adds a point to the object - The object must be a Point object or an np.ndArray
        Example:
        >class.addPoint(Point(5,7).coords)
        >class.addPoint(Point(5,7))


Polygon Class
-----------------------

**Creating a polygon class:**

>A = Polygon([Point1, Point2, Point3])

>A = Polygon([Point1.coords, Point2.coords, Point3.coords])

**Reading a specified file**

>A = Polygon([]).createFeatureFromFile('filename')
            
            
           Methods:
           # returns the coordinates of the end point of the polygon
           >class.getEndPoint()
           
           # determines if a point of is within the minimum bounding rectangle of the object
           The point it can be object of Point class or a list containing the coordinates, or an np.ndarray.
           >class.containsMBR(point)
           
           Examples:
               class.containsMBR(Point(5,3))
               class.containsMBR(Point(5,3).coords)
               class.containsMBR([5,3])
            
            # determines if a point is contained within the polygon
            >class.contains(point)
            
            The point it can be object of Point class or a list containing the coordinates, or an np.ndarray.
            Examples:
               class.contains(Point(5,3))
               class.contains(Point(5,3).coords)
               class.contains([5,3])

            # Plots the polygon. if you define a point, it will also be displayed`
            >class.plotPoints(self, point = None)
