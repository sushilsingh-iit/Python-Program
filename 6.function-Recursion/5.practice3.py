#waf to find factorial of n .(n is the parameter )
n = int(input("Enter your Number: "))

def print_fac(n):
    fact = 1
    
    # Check for negative numbers
    if n < 0:
        return "Factorial not found"
    
    # ERROR FIX 1 & 2: Change range start to 1, and indent the loop inside function
    for i in range(1, n + 1):
        fact = fact * i
    
    # ERROR FIX 3: Return statement must be OUTSIDE the loop
    return fact 

# ERROR FIX 4: You must actually call the function to see the result
print(print_fac(n))

# # mam method 
# def cal_fact(n):
#     fact = 1 
#     for i in range(1 , n+1):
#         fact *= i 
#     print(fact)

#  cal_fact(2)   



