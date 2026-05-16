import random

class NumberGuesser:
    def __init__(self, low=1, high=10, max_guesses=4, max_hints=3):
        self.low = low
        self.high = high
        self.number = random.randint(low, high)

        self.guesses_left = max_guesses
        self.hints_left = max_hints

        # precompute hint data (private methods)
        self._factors = self._get_factors()
        self._multiples = self._get_multiples()
        self._parity = self._get_parity()

    # ---------- PRIVATE METHODS ----------
    def _get_factors(self):
        return [i for i in range(1, self.number + 1) if self.number % i == 0]

    def _get_multiples(self):
        return [self.number * i for i in range(1, 6) if self.low <= self.number * i <= self.high * 10]

    def _get_parity(self):
        return "even" if self.number % 2 == 0 else "odd"

    # ---------- HINT SYSTEM ----------
    def give_hint(self):
        if self.hints_left <= 0:
            print("No hints left!")
            return

        choice = random.choice(["a", "b", "c"])
        self.hints_left -= 1

        if choice == "a":
            if self._factors and self._multiples:
                pick = random.choice(["factor", "multiple"])
            elif self._factors:
                pick = "factor"
            else:
                pick = "multiple"

            if pick == "factor":
                print("Hint (factor):", random.choice(self._factors))
            else:
                print("Hint (multiple):", random.choice(self._multiples))

        elif choice == "b":
            direction = random.choice(["larger", "smaller"])

            if direction == "larger":
                hint = random.randint(self.number + 1, self.high)
            else:
                hint = random.randint(self.low, self.number - 1) if self.number > self.low else self.number + 1

            print(f"Hint ({direction}):", hint)

        else:
            print("Hint (parity):", self._parity)

        print(f"Guesses left: {self.guesses_left}, Hints left: {self.hints_left}")

    # ---------- GAME LOGIC ----------
    def guess(self, value):
        if self.guesses_left <= 0:
            print("No guesses left! The number was:", self.number)
            return False

        if value == self.number:
            print("🎉 Correct! You guessed the number!")
            return True

        self.guesses_left -= 1

        if value < self.number:
            print("Too low!")
        else:
            print("Too high!")

        print(f"Guesses left: {self.guesses_left}, Hints left: {self.hints_left}")
        return False


# ---------- CHATBOT LOOP ----------
def main():
    game = NumberGuesser()

    print("Welcome to Number Guesser!")
    print(f"I'm thinking of a number between {game.low} and {game.high}.")
    print(f"You have {game.guesses_left} guesses. Type 'hint' for help.\n")

    while game.guesses_left > 0:
        user_input = input("Enter your guess or 'hint': ").lower()

        if user_input == "hint":
            game.give_hint()
            continue

        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a number or 'hint'.")
            continue

        if game.guess(guess):
            break

    else:
        print("Game over! The number was:", game.number)


main()