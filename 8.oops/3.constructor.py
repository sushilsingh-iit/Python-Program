# All classes have a function called _init_() , which is always executed when the
#claass is being initiated.

# creating class

#class student:                                     #creating object
#   def __init __(self ,fulname):                   # s1= student ("sushil")
#      self.name = fullname                         #print(s1.name)

#NOTE -  the self parameter is a referance to the current intance of the class, and is used to 
#access  variables that belong to the class.


class student:
    def __init__(self,fullname,marks):
        self.name = fullname # self is a first parameter
        self.marks = marks 
        print("creating new student in database..")


s1 = student("sushil singh",98)
print(s1.name,s1.marks)


s2 = student("karan",99)
print(s2.name,s2.marks)


# self is a first parameter
#     