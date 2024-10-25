import random
import matplotlib.pyplot as plt  # Corrected import statement

# had to move this outside the function to make it accisable to the new function 
options = ["heads", "tails"]

# Function for randomly generating heads or tails upon coin flip
def chances():
    input('Press Enter to flip the coin! ')
    coin_flip = random.choice(options)
    return coin_flip

# Function that will count how many heads or tails are generated
def flip_count(num_flips):
    heads_count = 0  
    tails_count = 0  
    for x in range(num_flips):
        if random.choice(options) == "heads":
            heads_count += 1
        else:
            tails_count += 1
    return heads_count, tails_count

# Get the number of flips from the user
num_flips = int(input("Enter the number of flips you want to do: "))
heads, tails = flip_count(num_flips)

# Print the results in a nice statement 
print("Heads: " + str(heads) + " Tails: " + str(tails))

# Plotting the Data by setting up graph characteristics 
labels = ["Heads", "Tails"]
counts = [heads, tails]

plt.bar(labels, counts, color = ['red', 'blue'])
plt.title("Coin flip results")
plt.xlabel("Outcome")
plt.ylabel("Count")

result = chances()
print("The Coin landed on:",result)

plt.show()




