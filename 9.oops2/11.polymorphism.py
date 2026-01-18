#operator overloading- 
# when the same operator is allow to have different according to the context.

print(1+2) #3
print("sushil"+"singh") #concatenate
print(type("suhsil"))
print([1,2,3,3]+[5,6,7,8])# merge
print(type([1,2,3,4]))


# The symbol is the same (+), but the behavior changes based on the input. 
# That is the essence of polymorphism.


# exampl- 

# a + b # addition     a.__add__(b)
# a - b # subtraction  a.__sub__(b)
# a * b #multiplication a.__mul__(b)
# a/b   #division      a.__truediv___(b)
# a%b #addition        a.__mod___(b) 


