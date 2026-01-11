#




# list method 
# list = [2,1,3]
# lis.append # adds one element at the end [2,1,3,4]
#
# list.sort ()  [1,2,3,4]
# list.sort(reverse = True )   # sorts in descending order   [3,2,1]
# list .reverse() #  reverse list [3,2,1]
# list.insert(idx,el)  # insert element at index


list = [2,3,1,4]
list.append(5)
list.sort()
print (list)


list1 = [3,4,5,1,7]
print(list1.sort(reverse=True))
print (list1)



list2 = ["banana", "apple" , "cherry"]
list2.sort()
print(list2)


list3 = ["a", "b", "c", "d"]
list3.reverse()
print(list3)


# list.insert (idx , el)

list4 = [2,3,1]
list4.insert(2,5) # second position 5 add 
print (list4)

# remove method 
list5 = [2,3,4,5,6,7,8,9]
list5.remove(4)
print(list5)


#pop method 
# remove element at idx 

list6 = [1,2,3,4,4,5]
list6.pop(2)
print(list6)