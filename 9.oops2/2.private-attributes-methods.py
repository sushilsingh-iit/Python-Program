#private(like) attributes and methods 
#conceptual Implementation in python

#private attributes and method are meant to be used only within  the class and are not 
#accessible from outside the class.

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #privete this thing



    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = account("1234","abcd")

print(acc1.acc_no)
acc1.reset_pass()



class person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = person()

print(p1.welcome())



