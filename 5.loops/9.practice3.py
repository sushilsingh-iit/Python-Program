# using fro loop 
# print the element of the following list using a loop.
#[1,4,16,25,36,49,64,61,100]
num = [1,4,16,25,36,49,64,61,100]
for el in num:
    print (int(el))



# search for a number x in this tuple using loops
# [1,2,16,25,36,49,64,81,100]
nums = [1,2,16,25,36,49,64,81,100,49]
x = 49

idx = 0
for el in nums:
    if (el == x):
       print ("number found in inx",  idx)
       break
    idx += 1 

# prigraming me this process called linear search.

