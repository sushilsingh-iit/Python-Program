# with open ("demo.txt","a") as f :
# data =f.read()

with open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/demo.txt", "w") as f:
    f.write("new data") # add new data in your file 
    
 