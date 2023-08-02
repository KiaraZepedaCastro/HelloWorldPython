# When naming classes, the name is capitalized and no underscores are used
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


# Object is an instance of a class
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 20
# point2.y = 40
# print(point2.x)
# point2.draw()

point3 = Point(10, 20)
point3.x = 30
print(point3.x)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()
