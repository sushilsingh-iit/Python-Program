#prioperty - we use @property decorator on any method in the class to use the 
# method as a property.

class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

        #percentage
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

        # def calcpercentage(self):
        #self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"




stu1 = student(98,97,96)
print(stu1.percentage)

stu1.phy = 77
print(stu1.percentage)

