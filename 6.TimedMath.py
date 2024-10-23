import random
import time

OPER = ["+", "-", "*", "/"]
MIN_OPER = -15
MAX_OPER = 15
total_problems = 10
# ranident is a method that will return a int from the specified range
def generate_problem():
    left = random.randint(MIN_OPER, MAX_OPER)
    right = random.randint(MIN_OPER, MAX_OPER)
    operator = random.choice(OPER)
    # use the python eval function rather than making seperate condtional if statements 
    expr = str(left) +  " " + operator + " " + str(right)
    ans = eval(expr)
    return expr, ans

expr, ans = generate_problem()

print(expr, ans)

wrong = 0
input("Press enter to start! ")
print("--------------------------------")

# time stamp in seconds 
start_time = time.time()

for i in range(total_problems):
    expr, ans = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(ans):
            break
        wrong += 1
        
# round time and find the total time
end_time = time.time()
total_time = round(end_time - start_time, 2)


print("--------------------------------")
print("Nice Work!", total_time, "Seconds! ")
        

