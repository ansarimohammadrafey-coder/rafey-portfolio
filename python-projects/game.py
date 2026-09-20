import random

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")

print("\nI have selected a number between 1 and 100.")
print("Try to guess it!")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")

        elif guess < secret_number:
            print("Too low! Try a higher number.")

        elif guess > secret_number:
            print("Too high! Try a lower number.")

        else:
            print("\nCongratulations!")
            print("You guessed the correct number!")
            print("Total attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid number.")

print("\nThanks for playing!")