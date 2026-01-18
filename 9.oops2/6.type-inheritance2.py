#multiple inheritance- 
# base1  base2 
#    !!!!!!!!
#  derived (child)


class a:
    vara = "welcome to var a "

class b:
    varb = "welcome to var b"

class c(a,b):
    varc = "welcome to var c "

c1 = c()

print(c1.varc)
print(c1.varb)
print(c1.vara)