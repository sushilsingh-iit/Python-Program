#a class method is bound to the class and receives the class as an implicit first argument.
# NOTE -- static method can not access or modify state and generally for utility.

class person:
    name = "sushil"
    def changename(self,name):
    

        #first method
        self.__class__.name = name


p1 = person()
p1.changename("singh ji")
print(p1.name)
print(person.name)




class person:
    name = "sushil"
    def changename(self,name):
        person.name = name  # second  method
        

       

p1 = person()
p1.changename("singh ji")
print(p1.name)
print(person.name)