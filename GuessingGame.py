#  Guessing Game by Code-Repeat
#  Follow me on Instagram @code-repeat

import random, sys


def guessTheNumber():
    #  Generate a  random number between 1 and 10
    number = random.randint(1, 10)
    for i in range(3):
        print("Guess a number between 1 and 10: ")
        guess = int(input())

        if guess < number:
            print('Too low')
        elif guess > number:
            print('Too high')
        elif guess == number:
            print("You guessed it!")
            ask_play = input("Do you want to play again? y/n ")
            if ask_play == "y":
                guessTheNumber()
            else:
                sys.exit()
        else:
            continue
    try_again = input("Would you like to try again? y/n: ")
    if try_again == "y":
        guessTheNumber()
    else:
        print("Ok. Bye-Bye!")
        sys.exit()


guessTheNumber()
