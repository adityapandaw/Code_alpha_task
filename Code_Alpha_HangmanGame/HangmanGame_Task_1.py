import random

words = ["apple", "table", "chair", "plant", "bread"]
word = random.choice(words)

guessed = ""
attempts = 6

print("Welcome to Hangman Game")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)
    print("Attempts left:", attempts)

    if display == word:
        print(" You Win!")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed += guess
        print(" Correct")
    else:
        attempts -= 1
        print(" Wrong")


if attempts == 0:
    print(" You Lose! Word was:", word)