# recursion - when a function called itself repeatedly
#prints n to 1 backwards 
# loop ka kaam recursion se kar sakte hai and recursion ka kaam loop se kar sakte hai 
def show(n):
   if (n==0): # base case 
        return
   print(n)
   show (n-1)
   print("End Layer")


show(7) # 5,4= n-1 ,3= n-2,2= n-3,1= n-4



# return n!

def fact(a):
    if (a == 1 or a == 0):
        return 1
    return fact(a-1) * a
print(fact(4))



# n! = (n-1)! * n    # recrense relation

# factorial(n) = factorial (n-1) * n
# factorial (n-1) = factorial(n-2)*(n-1)



