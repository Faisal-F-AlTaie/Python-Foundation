# if cheese is yes its 0.50 (captalize any inputs)
if cheese.capitalize() == "Y" :
  total += 0.50

# asking if you want tomatos
print("Would you like tomatos on your sandwhich")
tomatos = input("Y or N? :")

# if tomatos is yes then value is 0.25 (captalize any inputs)
if tomatos.capitalize() == "Y" :
  total += 0.25

# asking if you want leetuce
print("Would you like lettuce on your sandwhich")
lettuce = input("Y or N? :")

# if input is yes then value is 0.10 (captalize any inputs)
if lettuce.capitalize() == "Y" :
  total += 0.10

# asking if you want onions
print("Would you like onions on your sandwhich")
onions = input("Y or N? :")

# if input is yes then value is 0.10 (captalize any inputs)
if onions.capitalize() == "Y" :
  total += 0.10

# asking if you want kecheup
print("Would you like ketchup on your sandwhich")
ketchup = input("Y or N? :")


# asking if you want mayonnaise
print("Would you like mayonnaise on your sandwhich")
mayonnaise = input("Y or N? :")


# asking if you want mustard
print("Would you like mustard on your sandwhich")
mustard = input("Y or N? :")

# condements dont have statments because yes or no all vlues are 0

# round all numbers to the second decimal place and print the total
total = round(total, 2)
total = format(total, '.2f')
print(total)
