""" Part I: The Rectangle class"""
class Rectangle:

    #FIXME: implement the class here
    def __init__(self):
        self.width = 1
        self.height = 1


    def __init__(self, nwidth, nheight):
        self.width = nwidth
        self.height = nheight

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

"""Part II: The tester"""

#FIXME: Implement your tester in this cell
r1 = Rectangle(4, 40);
r2 = Rectangle(3.5, 35.9)

print("First Rectangle     Width:", r1.width, "Height:", r1.height, "Area:", r1.getArea(), "Perimeter:", r1.getPerimeter());
print("Second Rectangle     Width:", r2.width, "Height:", r2.height, "Area:", r2.getArea(), "Perimeter:", r2.getPerimeter());