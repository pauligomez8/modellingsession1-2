from point_class import Point

class ColorPoint(Point):
    def __init__(self, x, y, color):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be int or float")
        self.x = x
        self.y = y
        self.color = color
    def __str__(self):
        # overwrite the __str__ from the parent
        return f"{self.color}:cp<{self.x}, {self.y}>"

if __name__ == "__main__":
    p1 = ColorPoint(0, 0, "red")
    p2 = ColorPoint(10, 10, "green")
    print(p1.x, p1.y, p1.color)
    print(p2)
    # because I have not touched the def in here, it calls the parent method!
    print(p2.distance_origin())
    points = [p1, p2]
    print(points)
    points.append(Point(2,0))
    points.append(-1)
    points.sort()
    print(points)
    #p5 = ColorPoint("Bob", [1, 2, "James"], "red")
    #print(p5)
