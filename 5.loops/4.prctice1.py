# print the multipicatrion table of a number n.
n =  int(input ("Enter your Number :"))
i = 1 
while i <= 10:
    print(n*i)
    i +=1 



# print the element of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0 
while idx < len(nums):
    print(nums[idx]) # nums[0] , nums[1], nums[2]..
    idx += 1  # idx rename as i 


#search for a number x in this tuple using loop:
nums1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36  # Maan lijiye humein 36 dhoondna hai
i = 0

while i < len(nums1):
    if nums1[i] == x:  # Check karein agar current number x ke barabar hai
        print("Number", x, "mil gaya index", i, "par")
        break  # Number mil gaya toh loop aage chalane ki zaroorat nahi hai
    i += 1


# frome sradha mam 
nums2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49 
i = 0   # initialization 
while i < len(nums2):
    if (nums2[i] == x):
        print ("found at idx ", i)
    i += 1 