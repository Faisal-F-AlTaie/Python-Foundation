print("Welcome to my first game! ")
name = input("What is are your name? ")

age = int(input("What is your age? "))

print("hello", name)

health = 10
  
if age >= 18:
    print("You are old enough to play! ")
    
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("you are starting with", health, "health")
        print("Lets Play")
        left_or_right = input("First Choice... Left or Right (left/right)? ")
        if left_or_right == 'left':
            ans = input("Nice you followed the path and reached a lake... Do you swim across or go around (across/around) ")
            if ans == 'around':
                print('you went around and reached the other side of the lake')
            elif ans == "across":
                print('you manged to get across but you were bit by a fish and lost 5 health')
                health -= 5
                
            ans = input('You notice a house and a river. Which do you go to (river/house)? ')
            if ans == "house":
                print("You go o the house and are greeted by the owner... He does not like you and you lose 5 health")
                health -= 5  
                
                if health <= 0:
                    print("you now have zero health and you lost the game... ")
            else:
                print("Your survived. Congrats you are a winner! ")     
        else:
            print("You fell down a hole and lost! ")
    else:
        print("Goodbye, Hope to see you soon! ")
else:
    print("you are not old enough to play")
    

