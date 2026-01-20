# Method 2: Calculator using Functions (Better Practice)
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

print("1.Add  2.Subtract  3.Multiply  4.Divide")
choice = int(input("Choose (1/2/3/4): "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(a, b))
elif choice == 2:
    print("Result:", sub(a, b))
elif choice == 3:
    print("Result:", mul(a, b))
elif choice == 4:
    print("Result:", div(a, b))
else:
    print("Invalid choice")
