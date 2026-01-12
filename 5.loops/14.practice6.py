#WAP to find the sum of first n NUmber. (for ) # n - natural number 

n = int(input("Enter your number :"))
total_sum = 0

for i in range(1 , n+1):
    total_sum += i


print("total sum :", total_sum)     



# WHILE LOOP METHOD 

# N = R 
 

r = 6
sum = 0 
i = 1



while i <= r:
    sum += i
    i += 1
    print ("total sum ", sum)



# wap to find the factorial of first  numbers.(using for )
# factorial mean - fact(5) = 1*2*3*4*5
n = 5
fact = 9


for i in range(1,n+1):
    fact *= i
    print("Your factorial value :", fact)

