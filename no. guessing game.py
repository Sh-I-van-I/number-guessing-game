import random

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 10)
        self.attempts = 0

    def run(self):
        print("Welcome to the Number Guessing Game!")

        while True:
            guess = input("Guess the secret number (between 1 and 10): ")
            try:
                guess = int(guess)
                self.attempts += 1

                if guess < self.secret_number:
                    print("Too low! Try again.")
                elif guess > self.secret_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the secret number {self.secret_number} in {self.attempts} attempts!")
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()
