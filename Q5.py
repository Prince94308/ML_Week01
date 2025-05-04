import random

number = random.randint(1, 20)

for attempt in range(1, 6):
    guess = input("Attempt {}: Enter your guess: ".format(attempt))

    if not guess.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    guess = int(guess)

    if guess == number:
        print("Congratulations! You guessed it right!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

else:
    print("Sorry, you ran out of attempts. The number was {}.".format(number))
