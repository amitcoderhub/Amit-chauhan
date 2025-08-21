# Problem-1: Calculator using Class

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero not allowed"


calc = Calculator()

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, sub, mul, div): ").lower()

if operation == "add":
    print("Result:", calc.add(a, b))
elif operation == "sub":
    print("Result:", calc.subtract(a, b))
elif operation == "mul":
    print("Result:", calc.multiply(a, b))
elif operation == "div":
    print("Result:", calc.divide(a, b))
else:
    print("Invalid operation")
