# set.add(el)    # adds an element 
# set.remive(el)   # remove an element 
# set.clear ()    # empties the set 
# set.pop()      # removes a random value 
# set.union(set2)   # combine both set & return new 
# set.intersection(set2)   # combines common value & return new 


# set are mutable 
# set element are imutable 



# add method 
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("sushil")
# collection.add([1,2,3,3,])   # yuo can not add list 

collection.add((1,2,3,))


# print only 2 element 
collection.remove(2)
print (collection)



# clear method 


collection.clear()  # full collection are clear 

collection1 = {1,2,3,4,"sushil"}
collection1.clear()
print(len(collection1))

# pop method 

collection2 = {"apple ", "banana ", "cherry " , "hello"}
collection2.pop()
print(collection2)  # remove random element 



# both set method - combine both set value & return 

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))   #  NOTE THIS COMMAND
print(set1)
print(set2)


# intersection method

set3 = {2,3,4,5,6}
set4 = {6,7,8,9,10}

print(set3.intersection(set4))   # print common intersection 





