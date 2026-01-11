#myDict.keys()   # return all key 
# myDict.values()  # returns all values 
# myDict.items()  # return all values
# myDict.item()  # return the key according to value 
# myDict.update() # insert the specified items to the dictionary 


student ={
    "name" : "sushil singh",
    "subject" : {
        "physics" : 85,
        "math " : 49,
        "chemistry" : 80
    }
}


print(student.keys())
print(student.values())

# type cast any other type 
print(list(student.keys()))


print(student.items())



# access pair 

pairs = list(student.items())

print(pairs[1])


# myDit.get ,method 


# print(student["name1"]) # error
print(student.get("name1"))   # no Error 

# update method 

student.update({"location" : "Patna" , "village " : "surjanpur"})
print(student)


