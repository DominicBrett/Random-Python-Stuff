# Tell the bot how many times you want it to flip a heads in a row, bot will flip coins untill it flips that manyheads in a rows
import random

headsInARow = 0
headsInARowLimit = int(input("How many heads in a row do you want?"))
Attempts = 0

while headsInARow != headsInARowLimit:
    print("Flipping Coin")
    if random.random() < .5:
        print("Heads")
        headsInARow += 1
    else:
        print("Tails")
        headsInARow = 0
        Attempts += 1
print("It took " + str(Attempts) + " to get " + str(headsInARowLimit) + " heads in a row.")
