#nested dictionary in python
student ={
    "name" : "sushil singh",
    "subject" : {
        "physics" : 85,
        "math " : 49,
        "chemistry" : 80
    }
}


print(student)


# we call nested dictionary 


#print only one value 

print(student["subject"]["chemistry"])
print(len(student.keys()))


