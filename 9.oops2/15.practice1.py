#Question - define a employee class with attributes role, department and salary this class
# also showdetails ()method 

# create an engineer class thet inherits propeties from employee and has additional 
# attributes : name & age 


class Employee:  # Parent Class
    def __init__(self, role, dept, salary):
        self.role = role 
        self.dept = dept 
        self.salary = salary 

    def showdetails(self):
        print("Role = ", self.role)
        print("Dept = ", self.dept)
        print("Salary =", self.salary)

# 1. 'Engineer' must be a separate CLASS, not a function
# 2. It inherits from (Employee)
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
        # 3. Use super() to set the fixed values for this role
        super().__init__("Engineer", "IT", "75,000")

# --- usage ---

engg1 = Engineer("Sushil", "22")
engg1.showdetails()