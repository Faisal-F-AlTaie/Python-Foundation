import random
import time
import math

# https://www.w3schools.com/python/module_math.asp
oper_kg = ["+"]
oper_elementry = ["+", "-", "*"]

oper_middle_school = {
    "√":math.sqrt,
    "^": "**",
    "/": "/",
}
# lambda is a place holder 
oper_high_school = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "csc": lambda x: 1 / math.sin(x),
    "sec": lambda x: 1 / math.cos(x),
    "cot": lambda x: 1 / math.tan(x),
}


# Start Time and Beignning Statements 
input("Press Enter to Start! ")
print("----------------------------------------------")
wrong = 0
start_time = time.time()



# Kindergarden (kg) Section
total_problem_kg = 3
print("Starting the kindergarden Section. What do you remember from KG? ")
def generate_problem_kg():
    min_oper = 1
    max_oper = 10
    left = random.randint(min_oper, max_oper)
    right = random.randint(min_oper, max_oper)
    oper = random.choice(oper_kg)
    expr = str(left) +  " " + oper + " " + str(right)
    ans = eval(expr)
    return expr, ans

expr, ans = generate_problem_kg()

for i in range(total_problem_kg):
    expr, ans = generate_problem_kg()
    while True:
        guess = input("Problem Number " + str(i + 1) + ": " + expr + " = ")
        if guess == str(ans):
            break
        wrong += 1
print("---------------------------")



# Elementry Section
print("Starting the Elementry Section. What do you remember from grades 1-4? ")
total_problem_elementry = 3

def generate_problem_elementry():
    min_oper = 0
    max_oper = 20
    left = random.randint(min_oper, max_oper)
    right = random.randint(min_oper, max_oper)
    oper = random.choice(oper_elementry)
    expr = str(left) +  " " + oper + " " + str(right)
    ans = eval(expr)
    return expr, ans

expr, ans = generate_problem_elementry()

for i in range(total_problem_elementry):
    expr, ans = generate_problem_elementry()
    while True:
        guess = input("Problem Number " + str(i + 1) + ": " + expr + " = ")
        if guess == str(ans):
            break
        wrong += 1
print("---------------------------")



# Middle School Section
print("Starting the middle school section. what do you remember from grades 5-9? ")
total_problem_middle_school = 3

def generate_problem_middle_school():
    min_oper = -10
    max_oper = 40
    left = random.randint(min_oper, max_oper)
    oper = random.choice(list(oper_middle_school.keys()))

    if oper == "√":
        expr = f"√{left}"
        ans = round(math.sqrt(left), 2)  
    elif oper == "^":
        right = random.randint(1, 3)  
        expr = f"{left} ** {right}"
        ans = round(left ** right, 2)
    elif oper == "/":
        right = random.randint(1, max_oper)
        expr = f"{left} / {right}"
        ans = round(left / right, 2)
    else:
        expr = f"{left} {oper} {right}"
        ans = eval(expr)
    return expr, ans

expr, ans = generate_problem_middle_school()

for i in range(total_problem_middle_school):
    expr, ans = generate_problem_middle_school()
    while True:
        guess = input("Problem Number " + str(i + 1) + ": " + expr + " = ")
        if guess == str(ans):
            break
        wrong += 1
print("---------------------------")



# High School Section
print("Starting the High school section. What do you remember from grades 10-12? ")
print("Any Trig functions must be answered in radians and all answers must be to the nearest hundrenth!") 
total_problem_high_school = 3

def generate_problem_high_school():
    # Create a list of numbers rounded to two decimal places
    number = [round(1,2), round(math.sqrt(3) / 2, 2), round(math.sqrt(2) / 2, 2), round(1/2, 2), round(math.e, 2)]
    x = random.choice(number)
    oper = random.choice(list(oper_high_school.keys()))
    
    # logarithms separately because it only works with (+) numbers
    if oper == "log" and x <= 0:
        x = round(random.uniform(1, 10), 2) 

    # Generate the answer using the function from the dictionary and round to 2 decimal places
    ans = round(oper_high_school[oper](x), 2)
    
    # Create a readable expression string
    expr = f"{oper}({x})"
    
    return expr, ans

for i in range(total_problem_high_school):
    expr, ans = generate_problem_high_school()
    while True:
        guess = input(f"Problem Number {i + 1}: {expr} = ")
        try:
            if abs(float(guess) - ans) < 1e-2:  
                break
        except ValueError:
            print("Please enter a numerical answer.")
print("---------------------------")



# end time and final statement
end_time = time.time()
total_time = round(end_time - start_time, 2)
print("---------------------------------------------")
print("Nice Work!", total_time, "Seconds! ")
    
