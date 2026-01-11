# 1. Arithmetic Operators

# Used for mathematical calculations.

# Operator	Meaning	Example
# +	Addition	10 + 5 = 15
# -	Subtraction	10 - 5 = 5
# *	Multiplication	10 * 5 = 50
# /	Division	10 / 5 = 2.0
# %	Modulus (remainder)	10 % 3 = 1
# **	Exponent (power)	2 ** 3 = 8
# //	Floor division	10 // 3 = 3


a = 10
b = 3
print(a + b)
print(a // b)




# 2. Comparison (Relational) Operators

# Used to compare two values (returns True or False).

# Operator	Meaning
# ==	Equal to
# !=	Not equal to
# >	Greater than
# <	Less than
# >=	Greater than or equal
# <=	Less than or equal


c = 10
d = 5
print(c > d)
print(c == d)

# 3. Logical Operators

# Used to combine conditional statements.

# Operator	Meaning
# and	True if both conditions are true
# or	True if at least one condition is true
# not	Reverses the result

x = 10
y = 5
print(x > 5 and y < 10)
print(not(x == 10))



# 4. Assignment Operators

# Used to assign values.

# Operator	Example	Same as
# =	a = 10	—
# +=	a += 5	a = a + 5
# -=	a -= 5	a = a - 5
# *=	a *= 5	a = a * 5
# /=	a /= 5	a = a / 5


# 5. Bitwise Operators

# Used to work with binary numbers.

# Operator	Meaning
# &	AND
# `	`
# ^	XOR
# ~	NOT
# <<	Left shift
# >>	Right shift


#example
m = 5   # 0101
n = 3   # 0011
print(m & n)


# 6. Membership Operators

# Used to test if a value exists in a sequence.

# Operator	Meaning
# in	True if value exists
# not in	True if value does not exist

# Example:

# list1 = [1, 2, 3]
# print(2 in list1)
# print(5 not in list1)

# 7. Identity Operators

# Used to compare memory location.

# Operator	Meaning
# is	Same object
# is not	Different object

# Example:

# a = [1, 2]
# b = a
# print(a is b)

# 8. Ternary (Conditional) Operator

# Short form of if-else.

# a = 10
# b = 20
# max = a if a > b else b
# print(max)