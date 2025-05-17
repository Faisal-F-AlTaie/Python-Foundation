# Faisal Altaie
# Computing Science 10
# Henry Wise Wood School
# 2021-2022 semster 1
# October 14th, 2021

# the inputs for all vales that this program will check for
weight = float(input("weight? :"))
length = float(input("length? :"))
width = float(input("width? :"))
height = float(input("height? :"))

# fourmla for volume for conversion
vol = (length*width*height)/1000000

# using boolean values to repersent whats to heavy or whats to large
too_heavy = False
if weight > 27 :
  too_heavy = True

# using boolean values to repersent whats to heavy or whats to large
too_big = False
if vol > 0.1 :
  too_big = True

# if the values are neither big or heavy it will go through
if not too_big and not too_heavy :
  print('accepted')

# if ethe value is to heavy but not to big it only shows that its to heavy
if too_heavy and not too_big :
  print('too heavy')

# if value is to big but not to heavy it will only show that its to large
if not too_heavy and too_big :
  print('too large')

# if the package is to heavy and to large then print to heavy and large
if too_big and too_heavy :
  print('too heavy and too large')