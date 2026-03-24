from point_class import Point

class ColorPoint(Point):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def __str__(self):
        # overwrite the __str__ from the parent
        return f"{self.color}:cp<{self.x}, {self.y}>"

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

