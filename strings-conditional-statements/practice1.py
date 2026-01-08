# wap to check if a number entered bythe user is odd or even.



# 1. Take input and convert it to an integer
number = int(input("Enter a number: "))

# 2. Check the remainder when divided by 2
if number % 2 == 0:
    print("This is an EVEN number.")
else:
    print("This is an ODD number.")




#wap to find the greatest of 3 number entered by the user.

# WAP to find the greatest of 3 numbers entered by the user.

# 1. Take three inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# 2. Compare them
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The greatest number is: {largest}")

# WAP to check if a number a multiple of 7 or not .


num4 = int(input("Enter Your number :"))

if num4 % 7 == 0:
    print ("it mutiple it 7 ")
else:
    print("not mulitiple")