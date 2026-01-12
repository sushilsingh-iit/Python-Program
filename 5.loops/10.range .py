# range function returns a sequence of number , starting from 0 by defualt,
# 1 (by defult) , and stop before a specified number .
#range(start?,stop,step?)
 

seq = range(6)
# # print(seq[0])
# # print(seq[1])
# # print(seq[2])
# # print(seq[3])
# # print(seq[4])
# # print(seq[5])


for i in seq:
    print(i)



# # other method logical:

for x in range(10): # actual range is stoping value 
    print(x)

for y in range (2,10): # range(start,stop)
    print(y)

for z in range(2,10,2): #range(start,stop,spet(increasing value))
    print(z)




