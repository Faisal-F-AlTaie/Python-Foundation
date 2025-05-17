# Faisal Altaie
# Computing Science 10
# Henry Wise Wood School
# 2021-2022 semster 1
# October 14th, 2021

# the inputs for all values that this program will check for
weight = float(input("weight? :"))
length = float(input("length? :"))
width = float(input("width? :"))
height = float(input("height? :"))

# formula for volume for conversion
vol = (length*width*height)/1000000

# using boolean values to represent what's too heavy or what's too large
too_heavy = False
if weight > 27 :
  too_heavy = True

# using boolean values to represent what's too heavy or what's too large
too_big = False
if vol > 0.1 :
  too_big = True

# if the values are neither big nor heavy, it will go through
if not too_big and not too_heavy :
  print('accepted')

# if the value is too heavy but not too big, it only shows that it's too heavy
if too_heavy and not too_big :
  print('too heavy')

# if the value is too big but not too heavy,y it will only show that it's too large
if not too_heavy and too_big :
  print('too large')

# if the package is too heavy and too large, then print too heavy andtoo  large
if too_big and too_heavy :
  print('too heavy and too large')
