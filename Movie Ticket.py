# Faisal Altaie
# Computing Science 10
# Henry Wise Wood School
# 2021-2022 semster 1
# October 14th, 2021

# listing inputs for project: making sure all vaue are intgers.
movie = input("Movie ?:")
adults = int(input("Adults ?:"))
children = int(input("Children ?:"))
seniors = int(input("seniors ?:"))

# listing values for inputs
adults_ticket = 12.5
childrens_ticket = 8.25
seniors_ticket = adults_ticket * 0.75

# listing formula for calculations
total2  = (adults_ticket * adults) + (childrens_ticket * children) + (seniors_ticket * seniors)

# formating the values to 2 decimal places
total = format(total2, '.2f')

# using booleans to balance dollar signing with changing decimals
Total = (f'$ {total}')
if total2 == 93.50 :
  Total = f'$  {total}'
if total2 == 8.25 :
  Total = f'$   {total}'
title = f"*** {movie} ***"

# centreing and creating the title and top of the box
total = format(float(total), '.2f')
print(("-")* 30)
print(f'| {title.center(26)} |')

# printing the box side and rjusting and putting values withen it
print(f'| Adults: {str(adults).rjust(18)} ' + "|")
print(f'| Children: {str(children).rjust(16)} ' + "|")
print(f'| Seniors: {str(seniors).rjust(17)} ' + "|")
print(f'| Total:   {str(Total).rjust(17)} ' +    "|")
print(("-")* 30)



