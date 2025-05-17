# Faisal Altaie
# Computing Science 10
# Henry Wise Wood School
# 2021-2022 semster 1
# October 1st, 2021

# input dollar value as a decimal
dollar_amount = float(input('Enter a dollar amount: '))

# value of all the coins defined
quarters = 0.25
penny = 0.01
nickel = 0.05
dime = 0.10

# number of each coin
q = 0
p = 0
n = 0
d = 0

# run a while loop and stop when it hits the maximum amount of coins it hits: we also round nearest second point
while (dollar_amount >= quarters) :
  dollar_amount = round(dollar_amount - quarters,2)
  q += 1

# run a while loop and stop when it hits the maximum amount of coins it hits: we also round nearest second point
while (dollar_amount >= dime) :
  dollar_amount = round(dollar_amount - dime, 2)
  d += 1

# run a while loop and stop when it hits the maximum amount of coins it hits: we also round nearest second point
while (dollar_amount >= nickel) :
  dollar_amount = round(dollar_amount - nickel,2)
  n += 1

# run a while loop and stop when it hits the maximum amount of coins it hits: we also round nearest second point
while (dollar_amount >= penny) :
  dollar_amount = round(dollar_amount - penny,2)
  p += 1

# print coin amount via formula provided
print(f'quarters:{q}; dimes:{d}; nickels:{n}; pennies:{p}')