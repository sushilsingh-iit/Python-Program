#question- define a circle class to craete a circle with radius r using the contructor.
# define an area() method of the class which calculates the area of the circle.
# define a perimeter() method of the class which allows you ti calculate the parameter of the circle.

# rdius - pi.r'2
# perimeter - 2.pi.r
class circle:
    def __init__(self,radius):
        self.radius = radius


    def area(self):
        return (22/7)  * self.radius ** 2 
    
    def perimter(self):
        return 2* (22/7) *self.radius
    

c1 = circle(21)
print(c1.area())
print(c1.perimter())
