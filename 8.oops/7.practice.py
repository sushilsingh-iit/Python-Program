# create student class that takes name and marks of 3 subject as argument in constructor.
#then create a method to print the average.


class Student:
    college_name = "IIT Patna"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome Student", self.name, "Marks:", self.marks)


s1 = Student("sushil", 99)
s2 = Student("raj", 98)
s3 = Student("vishal", 97)

s1.welcome()
s2.welcome()
s3.welcome()

avg = (s1.marks + s2.marks + s3.marks) / 3

print("Students:", s1.name, s2.name, s3.name)
print("Average Marks:", avg)
