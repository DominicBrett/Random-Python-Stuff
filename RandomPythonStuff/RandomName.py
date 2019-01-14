# Generates random letters until your word is spelt
import string
import random

randomText = ""
Attempts = 0
wordToWrite = input("What word would you like to generate using random letters?")

while wordToWrite not in randomText:
    letter = random.choice(string.ascii_letters.lower())
    randomText += letter
    Attempts += 1
    print(letter)
print("Took " + str(Attempts) + " letters to generate word '" + wordToWrite + " '.")