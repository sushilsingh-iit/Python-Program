# method that do not use the sel parameter(work at class level)
#class student:
#@static method   # decorator
#def collage():
# print("abc collage")
# NOTE- decorators allow to us to wrap another function in order to extend the 
# behavior of the wrapped function , without permenatly modifying it.


class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod

    def hello():
        print("hello")

    def collage():
        print("abc collage")

s1 = student("sushil" ,98)
s1.name
print(s1.name,s1.marks)
s1.hello()