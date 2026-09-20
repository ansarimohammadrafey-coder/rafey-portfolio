import random

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("\nEnter your guess (1-100): "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100.")

        elif guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("\nCongratulations! 🎉")
            print("Correct guess!")
            print("Total attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid number.")

print("\nThanks for playing!")