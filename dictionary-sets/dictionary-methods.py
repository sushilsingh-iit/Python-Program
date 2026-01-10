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

# type ncast any other type 
print(list(student.keys()))



