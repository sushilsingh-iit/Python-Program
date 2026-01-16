# attributes is data 
# attributes is two type 
# 1. class attributes
# 2.instance attributes 

class student:
    collage_name = "IIT Patna"
    name = "singh" #class attributes 
    def __init__(self,name,marks):
        self.name = name  # object attributes
        self.marks = marks
        print("adding new student database")


s1 = student ("sushil", 00)
print(s1.name, s1.marks)  # pint sushil because  = object attr > class attr
print(s1.collage_name)