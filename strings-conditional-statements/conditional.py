# if - elif - else (asysntax 
# if (condition ):
#statement1 
#elif (condition):
# statment2 
# else :
# statement N



# Assuming you have an age variable, e.g., age = int(input("Enter age: "))
age = 18
if age >= 50:
    # We check 50+ first, otherwise the 18+ check would "steal" these cases
    print("You are over age")

elif age >= 18:
    # If we are here, we already know age is LESS than 50
    print("Welcome boss")

else:
    # We don't need a condition here. 
    # If it's not >= 50 and not >= 18, it MUST be < 18.
    print("You are a child")






num = 7 
if (num >2):
    print ("greater the 2")
if (num > 3):
    print ("graeter than 3 ")