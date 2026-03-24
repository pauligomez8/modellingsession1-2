
class Point:
    def __init__(self, x, y):
        """
        Initialize a point with x,y coordinates
        :param x: the x coordinate
        :param y: the y coordinate
        """
        self.x = x
        self.y = y
    def __str__(self):
        """
        Return a string representation of the point
        :return: p<x,y>
        """
        return f"p<{self.x},{self.y}>"
    def __repr__(self):
        return self.__str__()
    def distance_origin(self):
        """
        Return the distance from the origin to the point
        :return: float
        """
        return (self.x**2 + self.y**2)**0.5
    def distance_other(self, other):
        """
        Return the distance from the other point to the point
        :param other: another Point
        :return: the distance from the other point to the point
        """
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    def __lt__(self, other):
        """
        Compare two point objects
        :param other: the other point object
        :return: bool True or False
        """
        if isinstance(other, (int, float)):
            return self.distance_origin() < other
        return self.distance_origin() < other.distance_origin()
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.distance_origin() == other
        return self.distance_origin() == other.distance_origin()
    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other) # returns a new point!
        raise TypeError("Can only multiply a Point by an int!")
    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.distance_origin() > other
        return self.distance_origin() > other.distance_origin()
if __name__ == '__main__':
    # instantiate the point class
    p1 = Point(1, 2)
    p2 = Point(x=3, y=4)
    print(p1.x, p1.y)
    print(p1)
    p3 = Point(4, 3)
    print(p3.distance_origin())
    p4 = Point(12, 5)
    print(p4.distance_origin())
    points = [p1, p2, p3, p4, Point(-2, 6)]
    points.append(Point(-5, -5))
    # x coordinate of the 5th point in the list
    print(points[4].x)
    print(points[5].distance_origin())
    # print the entire list
    print(points)
    points.sort()
    print(points)
    points.append(7)
    points.sort()
    print(Point(7, 11).distance_other(Point(7, 15))) # expect 4
    print(p2 == p3)
    print(p2.distance_origin(), p3.distance_origin())
    print(p2 * 4)
    print(p2 * 4.2)

