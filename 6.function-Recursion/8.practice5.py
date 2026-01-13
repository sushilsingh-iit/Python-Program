# write a recursion function to calculate the sum of first n natural numbers.


def cal_sum(n):
     # Base Case: If n is 0 or 1, the sum is just n
    if n <= 1:
        return n
    
    # Recursive Step: n + sum of (n-1)
    else:
        return n + cal_sum(n - 1)


num = 5
result = cal_sum(num)

print(f"The sum of the first {num} numbers is: {result}")



