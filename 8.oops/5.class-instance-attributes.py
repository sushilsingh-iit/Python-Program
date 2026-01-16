# attributes is data 
# attributes is two type 
# 1. class attributes
# 2.instance attributes 

class student:
    collage_name = "IIT Patna"
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
        print("adding new student database")


s1 = student ("sushil", 00)
print(s1.name, s1.marks)
        
