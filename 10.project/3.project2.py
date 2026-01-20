# Smart Python Calculator
# calculator.py (Main Code – OOP Based)
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


def main():
    calc = Calculator()

    while True:
        print("\n--- Smart Python Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Thank you for using Calculator")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", calc.add(a, b))
        elif choice == "2":
            print("Result:", calc.subtract(a, b))
        elif choice == "3":
            print("Result:", calc.multiply(a, b))
        elif choice == "4":
            print("Result:", calc.divide(a, b))


if __name__ == "__main__":
    main()
