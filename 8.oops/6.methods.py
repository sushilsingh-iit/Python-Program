#methods are functions thet belong to objects.

# craeting class                                  # creating object 
# class student:                                  #s1 = student("karan")
#   def __init__(self,fullname):                  #s1.hello
#       self.name = fullname

# def hello (self)
# print("hello", self.name)

class student:
    collage_name = "IIT Patna"
    
    def __init__(self , name , marks ):
        self.name = name 
        self.marks = marks
        
    def welcome(self):
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks



s1 = student ("lucky", 77)
s1.welcome()
print(s1.get_marks())



