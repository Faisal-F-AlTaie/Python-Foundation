# Faisal Altaie
# Computing Science 10
# Henry Wise Wood School
# 2021-2022 semster 1
# October 14th, 2021

# repersenting out veriables and making them input values
starting_n = int(input("Enter the starting Number:"))
ending_n = int(input("Enter the ending Number:"))

list_n = []

# Create new list of numbers
for x in range(starting_n, ending_n + 1):
    list_n.append(x)

y = 0

if starting_n > ending_n:
    print("INVALID")

# Calculate the total sum
for x in list_n:
    y = y + x

# Print the numbers
for x in list_n:
    if x == ending_n:
        print(x, end=" = ")
        print(y)
    else:
        print(x, end=" + ")
