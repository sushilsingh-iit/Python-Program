class student:
    #defult constructors
    def __init__(self):
        pass 

    #parameterrized constructors

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
        print ("adding new student in database..")

s1 = student("sushil",90)
print(s1.name,s1.marks)

s2 = student("karan",89)
print(s2.name,s2.marks)


# run best sutable constructor at this time 

