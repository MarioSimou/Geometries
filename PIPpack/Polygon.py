from Geom import *
from Line import *
import matplotlib.patches as patches
import matplotlib.pyplot as py


class Polygon(Line,Geom):
    '''
       Documentation:
           Line Class
       Instructions:
           A line can be constructed:
               CAUTION: The Line class is based to the Point class for its construction. ONLY Point class objects are acceptable

               # Specifying a list which contains all the Point's class objects
                   Both examples below are threaded the same

               A = Polygon([Point1, Point2, Point3])
               A = Polygon([Point1.coords, Point2.coords, Point3.coords])

               # Reading a specified file
                   The file reading is based on the method of numpy package, genfromtxt (see https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.genfromtxt.html)

               A = Polygon([]).createFeatureFromFile('filename')

       Methods:
           class.getEndPoint()
           # returns the coordinates of the end point of the polygon

           class.containsMBR(point)
           # determines if a point of is within the minimum bounding rectangle of the object
           The point it can be object of Point class or a list containing the coordinates, or an np.ndarray.

           Examples:
               class.containsMBR(Point(5,3))
               class.containsMBR(Point(5,3).coords)
               class.containsMBR([5,3])

            class.contains(point)
            # determines if a point is contained within the polygon
            The point it can be object of Point class or a list containing the coordinates, or an np.ndarray.

            Examples:
               class.contains(Point(5,3))
               class.contains(Point(5,3).coords)
               class.contains([5,3])

            class.plotPoints(self, point = None)
            # Plots the polygon
            if you define a point, it will also be displayed

    '''

    # overrides the getEndPoint method of Geom superclass
    def getEndPoint(self):
        return self.getStartPoint() # starting point = ending point

    # determines if a point is contained in the minimum bounding rectangle
    def containsMBR(self, point):
        # checks if the imported point is instance of Point class
        if isinstance(point,Point) or isinstance(point,np.ndarray) or isinstance(point,list):
            # gets the Minimum Boundary Rectangle extent
            (xmin,ymin),(xmax,ymax) = self.getMBR()
            # determines the xp and yp coordinates of the object. The point can be Point class object, list or np.ndarray
            try:
                xp,yp = point.X,point.Y # TRY for Point class
            except Exception:
                try:
                    xp,yp = point[0], point[1] # TRY for list or np.ndarray
                    print(xp)
                    print(yp)
                except Exception:
                    print('[The point\'s location cannot be identified. Read the documentation for which datatypes are compatible with the method]')
            # initial condition
            contains = False
            if xp >= xmin: # checks if the x coordinate of point is greater or equal of xmin
                if xp <= xmax: # checks if the x coordinate of the point is less or equal of xmax
                    if yp >= ymin: # checks if the y coordinate of the point is greater or equal of ymin
                        if yp <= ymax: # checks if the y coordinate of the point is less ore equal fo ymax
                            contains = True
        else:
            raise Exception('[ Non Point object. Create a Point object and call the method again. ]')
        return contains

    def contains(self,point):
        if isinstance(point,Point) or isinstance(point,np.ndarray) or isinstance(point,list):
            # VARIABLES
            # number of nodes + the starting point
            n = self.getNumPoints()+1
            # condition
            inside = False
            # points locations
            try:
                xp,yp = point.X,point.Y # TRY for Point class
            except Exception:
                try:
                    xp,yp = point[0], point[1] # TRY for list or np.ndarray
                except Exception:
                    print('[The point\'s location cannot be identified. Read the documentation for which datatypes are compatible with the method]')
            # polygon coordinates
            # defines the nodes of the polygon
            # the starting point is also added
            poly = zip(self.getXVector()+[self.getStartPoint()[0]],self.getYVector()+[self.getStartPoint()[1]])
            # starting point coordinates
            p1x, p1y = self.getStartPoint()[0], self.getStartPoint()[1] # coordinates of the first point

            # Check if the point is within the minimum boundary rectangle (MBR)
            if self.containsMBR(point):
                # Loop over all the edges
                for i in range(n + 1):
                    p2x, p2y = poly[i % n] # the next point of the starting point (constructs edge)
                    # checks the orientation of points
                    # checks if the point intersects the edge
                    # if the imported point is not along the edge and the coordinates of edges are not the same
                    if self.isIntersect(Point(p1x, p1y), Point(p2x, p2y), Point(xp, yp)) and [p1x,p1y] != [p2x,p2y]:
                        return 'Point Along the Boundaries'
                    if yp > min(p1y, p2y):
                        if yp <= max(p1y, p2y):
                            if xp <= max(p1x, p2x):
                                if p1y != p2y:
                                    xints = (yp - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                                if p1x == p2x or xp <= xints:
                                    inside = not inside
                    p1x, p1y = p2x, p2y
        else:
            raise Exception('[ The points are not instances of Point Class. Create the points elements and try again. ]')

        return inside


    # Method overloading
    def plotPoints(self, point = None):
        x = self.getXVector() # x coordinates
        y = self.getYVector() # y coordinates
        if point is not None:
            # VARIABLES
            # get Object Coordinates
            if isinstance(point,Point) or isinstance(point,list) or isinstance(point,np.ndarray):
                try:
                    (xmin, ymin), (xmax, ymax) = self.getMBR() # set the polygons extent
                    height = ymax - ymin # defines the height of the MBR
                    width = xmax - xmin # defines the width of the MBR
                    try:
                        xp,yp = point.X, point.Y # gets the X and Y coordinates of the Point
                    except Exception:
                        try:
                            xp = point[0]  # gets the X and Y coordinates of the Point (if point is list or np.ndarray)
                            yp = point[1]  # gets the X and Y coordinates of the Point  if point is list or np.ndarray)
                        except Exception:
                            print('[ The location of the imported point cannot be identified. Read the documentation how that method works]')
                    # PLOTTING
                    # Create rectangle patch
                    rectangle = py.Rectangle((min(x),min(y)),width,height, linewidth= 2, edgecolor='r', facecolor='none', linestyle='dashdot')
                    py.gca().add_patch(rectangle)
                    # Create Polygon patch
                    # sorted(zip(x,y)) = concatenate x,y list into tuples, and then sort the tuple
                    Poly = py.Polygon(zip(x,y), closed=True, fill='blue',lw = 2, alpha = 0.2) # sorted
                    py.gca().add_patch(Poly)
                    py.plot(xp,yp, 'bs') # set point location
                    py.xlabel('X-Coordinates') # set X axes
                    py.ylabel('Y-Coordinates') # set Y axes
                    py.axis([min(min(x),xp)-2,max(max(x),xp)+2,min(min(y),yp)-2,max(max(y),yp)+2]) # sets the extent of the plot
                    py.show() # shows the plot
                except Exception:
                    print('[ Error during the plotting. Unknown Reason ]')
            else:
                raise Exception('[ Non Point object. Create a Point object and call the method again. ]')
        else:
            Poly = py.Polygon(zip(x, y), closed=True, fill='blue', lw=2, alpha=0.2)
            py.gca().add_patch(Poly)
            py.xlabel('X-Coordinates')  # set X axes
            py.ylabel('Y-Coordinates')  # set Y axes
            py.axis([min(x) - 2, max(x) + 2, min(y) - 2, max(y) + 2])  # sets the extent of the plot
            py.show()  # shows the plot



