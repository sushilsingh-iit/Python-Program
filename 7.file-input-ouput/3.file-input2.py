# writing to a file 

# f = open("demo.txt", "w")
# f.write("this is a new line ")


# f = open("demo.txt","a")
# f.write("this is a new line")

f = open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/demo.txt", "w")
f.write("welcome to my git and girthub")
f.close



# append 

f = open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/demo.txt", "a")
f.write("\nthen i will move to dsa") # \n for next line 
f.close


