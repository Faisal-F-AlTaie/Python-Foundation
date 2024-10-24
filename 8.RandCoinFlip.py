import random 

def chances():
    input('Press Enter to flip the coin! ')
    options = ["heads", "tails"]
    coin_flip = random.choice(options)
    return coin_flip

result = chances()

print("The Coin landed on:",result)


