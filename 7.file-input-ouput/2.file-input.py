# print only one line 
f = open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/demo.txt", "r")
line  = f.readline()
print(line )

line2 = f.readline()
print(line2)
print(type(line))
f.close()


# data = f.raed() # read entire file 
# data = f.raedline  # read one line at a time 