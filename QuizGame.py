print('Welcome to my Computer Systems Quiz! ')
playing = input('Do you want to play? ')

if playing != str('yes').lower():
    print("Sorry to see you go")
    quit()
else:
    print("Okay! Let's Play friend! ")
    score = 0
    
answer = input("What does CPU stand for? ")
if answer == str("central processing unit").lower():
    print('Correct, Excellent Work!')
    score += 1
else:
    print("sorry thats incorrect! Check Your Spelling if you think your right :)")
   
    
answer = input("What does RAM stand for? ")
if answer == str("random access memory").lower():
    print('Correct, Excellent Work!')
    score += 1
else:
    print("sorry thats incorrect! Check Your Spelling if you think your right :)")
    

answer = input("What does NPU stand for? ")
if answer == str("neural processing unit").lower():
    print('Correct, Excellent Work!')
    score += 1
else:
    print("sorry thats incorrect! Check Your Spelling if you think your right :)")
 
    
answer = input("What does SSD Stand for? ")
if answer == str("solid state drive").lower():
    print('Correct, Excellent Work!')
    score += 1
else:
    print("sorry thats incorrect! Check Your Spelling if you think your right :)")
 
    
answer = input("What does HD stand for? ")
if answer == str("hard drive").lower():
    print('Correct, Excellent Work!')
    score += 1
else:
    print("sorry thats incorrect! Check Your Spelling if you think your right :)")
    
    
answer = input("What does PSU stand for? ")
if answer == str("power supply").lower():
    print('Correct, Excellent Work!')
    score += 1
else:
    print("sorry thats incorrect! Check Your Spelling if you think your right :)")
    

print("You got " + str(score) + " Questions Correct out of 6")