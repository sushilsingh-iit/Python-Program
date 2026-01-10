#WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# start with an empty dictionary & add by one . Use subject nam eas key & marks as value .


mark = {}

x = int(input("Enter Phy : "))
mark.update({"Phy" : x})

x = int(input ("Enter Che : "))
mark.update({"Che" : x})


x = int(input ("Enter Math : "))
mark.update({"Math" : x})

print(mark)




# figure out a way to store 9 & 9.0 as seprate value in the set. 
# (YOU CAN TAKE HELP OF BUILD DATE TYPE)



my_set = set()

# 2. Add 9 (integer) paired with its type
my_set.add((9, int))

# 3. Add 9.0 (float) paired with its type
my_set.add((9.0, float))


print(my_set)
print(len(my_set))  # give 2 element that proved it .)



# other possible solution 
# values = {
#     ("float",9.0),
#     ("int",9)

# }
# print(values)
# print(len(values))

# complete set 
      