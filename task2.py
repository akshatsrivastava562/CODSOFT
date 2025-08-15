def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Simple Calculator")
print("Choose operation: +, -, *, /")
op = input("Enter operation: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if op == "+":
    result = add(a, b)
elif op == "-":
    result = subtract(a, b)
elif op == "*":
    result = multiply(a, b)
elif op == "/":
    if b != 0:
        result = divide(a, b)
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"

print("Result:", result)
