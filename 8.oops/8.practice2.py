# create student class that takes name and marks of 3 subject as argument in constructor.
#then create a method to print the average.
# by shradha mam

class student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hi",self.name,"your average score is: ", sum /3)

s1 = student("tonny stark",[99,98,97])
s1.get_avg()
# let supose i change my student name 
s1.name = "sushil singh"
s1.get_avg()