# write a recursion function to calculate the sum of first n natural numbers.

def calc_sum(n):
    if (n==0):
        return 0
 
    return calc_sum(n-1) + n


print(calc_sum(3))
print(sum)


# write a recursion function to print all element in aa list.
# hint - use list & index as parameter
# idx = ["a", "b", "c", "d"]


def print_list(list,idx=0):
    if (idx == len (list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","litchi","apple","banana"]

print_list(fruits)
