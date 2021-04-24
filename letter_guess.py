import random
import string

def letter_guess():
    answer = random.choice(string.ascii_letters)
    print("Important! The game is case sensitive")
    while True:

        user_guess = input("What is your guess: ")
        if user_guess == answer:
            print(f"Correct! your guess {user_guess} is same as the character chosen by the computer")
            break
        if user_guess != answer:
            if user_guess.lower() == answer:
                print(f"You have type the character {user_guess} with Upper Case")
            elif user_guess.upper() == answer:
                print(f"You have type the character {user_guess} with Lower Case")
            else:
                print (f"The computer's character is {answer}")

letter_guess()
