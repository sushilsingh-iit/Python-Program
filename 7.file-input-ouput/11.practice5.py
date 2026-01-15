#from a file containing number seprated by comma , print the count of even numbers.
# 1,2,3,4,5,55,,57,58,60

# with open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/practice2.txt","r") as f:
#     data = f.read()
#     print(data)


    # num = ""
    # for i in range(len(data)):
    #     if (data[i] == ","):
    #         print(int(num))
    #         num = ""

    #     else:
    #         num += data[i]

    # other method 
count = 0
with open("/home/rdx/Python-Programs/Python-Program/7.file-input-ouput/practice2.txt","r") as f:
        data = f.read()
        

        nums = data.split(",")
        for val in nums:
            if (int(val) % 2 == 0):
                  count += 1
               

print(count)
