import random


def guessing_game():
    answer = random.randint(0, 100)
    score = 100

    while True:
        user_guess = int(input("What is your guess? "))
        if user_guess == answer:
            print(f"Right! The answer is {user_guess} and your score is {score}")
            break
        if user_guess < answer:
            score = score - 10
            print(f"Your guess of {user_guess} is too low! Your score is {score}")
        else:
            score = score - 10
            print(f"Your guess of {user_guess} is too high! Your score is {score}")


guessing_game()
