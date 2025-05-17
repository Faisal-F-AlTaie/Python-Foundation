import math

num1 = float(input("Please Enter the first Number: "))
num2 = float(input("Please Enter the second Number: "))

oper = input("Please Enter an operation (+, -, *, /): ")

# Form the expression based on the user input
if oper in ["+", "-", "*", "/"]:
    expr = f"{num1} {oper} {num2}"
    ans = eval(expr)
    print(f"Result: {ans}")
else:
    print("Invalid operation")
