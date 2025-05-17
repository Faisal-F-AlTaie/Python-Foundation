# Faisal Altaie
# Computing Science 10
# Henry Wise Wood School
# 2021-2022 semster 1
# October 1st,

# create list to organize values in correct order
jump_list = []

# input values of all the jumps as decimal value
jump_1 = float (input("jump #1:"))
jump_2 = float (input("jump #2:"))
jump_3 = float (input("jump #3:"))
jump_4 = float (input("jump #4:"))

# organize all jumps in the list via append
jump_list.append(jump_1)
jump_list.append(jump_2)
jump_list.append(jump_3)
jump_list.append(jump_4)

# remove value via pop (get rid of lowest value) and sort
jump_list.sort()
jump_list.pop(0)

# average of all the jumps
average = (sum(jump_list)/len(jump_list))


# printing average in console
print (f'Average = {average}')
