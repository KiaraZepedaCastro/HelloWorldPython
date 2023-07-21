# When naming classes, the name is capitalized and no underscores are used
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


# Object is an instance of a class
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 20
point2.y = 40
print(point2.x)
point2.draw()