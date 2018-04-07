# Geometries
Geometries repository
------------------------------------------------

**Geom Class Methods**

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
        
        
        
**Point Class**
Instructions:
   A point can be constructed:
> A = Point(5,7,1) # 5,7,1 correspond to the X,Y and Z coordinates
> A = Point(5,7) # 5,7 correspond to the X and Y coordinates. Z is treated as zero value
> A = Point([5,7,1]) # a list is used to construct the object. The list MUST contains 3 elements
    
        Methods:
        class_name.coords  = returns the coordinates of the object in a list
        class_name.X = returns the X coordinate of the object
        class_name.Y = returns the Y coordinate of the object
        class_name.Z = returns the Z coordinate of the object
        class_name.getStartPoint = returns the coordinates of the point. [ class_name.getStartPoint = class_name.coords =                               class_name.getEndPoint ]
        class_name.getEndPoint = returns the coordinates of the point. [ class_name.getStartPoint = class_name.coords =                                 class_name.getEndPoint ]
        class_name.addPoint = Point object cannot add another point
    
