# Geometries
Geometries repository
------------------------------------------------

**Geom Class**

__CAUTION : Geom class cannot be instantiated__

__Methods:__

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
