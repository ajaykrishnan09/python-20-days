# guess_number.py
# Day 3 - Guess the Number (Replay + Random Range)
#
# What this program does:
# - Plays a "guess the number" game.
# - Round 1 uses a fixed range 1..10.
# - Round 2+ uses a RANDOM range within 1..100 (e.g., 10..25, 42..99).
# - User can play multiple rounds and choose when to quit.
# - User can type 'q' to quit a round immediately.

import random  # random gives us random numbers (secret number + random ranges)


def ask_yes_no(prompt: str) -> bool:
    """
    Ask a yes/no question until the user types a valid response.
    Returns:
        True  -> if user answers yes (y/yes)
        False -> if user answers no  (n/no)

    Why we use this:
    - Users might type random things like "maybe" or "sure".
    - This function keeps asking until we get a clear yes/no.
    """
    while True:
        answer = input(prompt).strip().lower()  # normalize input (remove spaces, make lowercase)

        # If the user typed something meaning "yes"
        if answer in ("y", "yes"):
            return True

        # If the user typed something meaning "no"
        if answer in ("n", "no"):
            return False

        # If we got here, the input was not valid
        print("Please type 'yes' or 'no' (or y/n).")


def random_range_within_100() -> tuple[int, int]:
    """
    Create a random inclusive range (low, high) inside 1..100 where low < high.

    Example outputs:
        (1, 10)
        (10, 25)
        (42, 99)

    How it works:
    - Pick a random 'low' between 1 and 99
    - Pick a random 'high' between low+1 and 100
      (so high is always bigger than low)
    """
    low = random.randint(1, 99)         # randint(a, b) returns a number between a and b inclusive
    high = random.randint(low + 1, 100) # ensure high is always > low
    return low, high


def play_round(low: int, high: int) -> None:
    """
    Play ONE round of the guessing game using the provided range.

    Rules:
    - User has ONLY 3 valid attempts per round
    - Invalid input or out-of-range guesses do NOT count as attempts
    - Typing 'q' quits the round early
    """
    secret_number = random.randint(low, high)
    attempts = 0
    MAX_ATTEMPTS = 3

    print("\n=== GUESS THE NUMBER ===")
    print(f"I am thinking of a number between {low} and {high} (inclusive).")
    print(f"You have {MAX_ATTEMPTS} attempts.")
    print("Type 'q' to quit this round.\n")

    while attempts < MAX_ATTEMPTS:
        guess = input("Enter your guess: ").strip()

        # Allow user to quit the round early
        if guess.lower() == "q":
            print("You quit this round.")
            return

        # Validate numeric input
        if not guess.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess_num = int(guess)

        # Validate range
        if guess_num < low or guess_num > high:
            print(f"Out of range! Please guess between {low} and {high}.")
            continue

        # Count ONLY valid guesses
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts

        if guess_num < secret_number:
            print(f"Too low! Attempts left: {remaining}")
        elif guess_num > secret_number:
            print(f"Too high! Attempts left: {remaining}")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            return

    # If we exit the loop, attempts are exhausted
    print(f"\n❌ Out of attempts! The number was {secret_number}.")


def main() -> None:
    """
    Main program controller:
    - Runs multiple rounds
    - Changes the range after the first round
    - Asks the user after each round if they want to play again
    """
    print("Welcome! Let's play Guess the Number.")

    round_number = 1  # used to make round 1 have a fixed range

    # Outer loop: controls multiple rounds ("play again?")
    while True:
        # Round 1 is fixed: 1..10
        if round_number == 1:
            low, high = 1, 10
        else:
            # Round 2+ uses a random range within 1..100
            low, high = random_range_within_100()

        # Play one round (this will return when round is over)
        play_round(low, high)

        # After a round ends, ask if user wants another round
        if not ask_yes_no("\nDo you want to play again? (yes/no): "):
            print("Goodbye!")
            break  # break exits the outer loop and ends the program

        # If user wants to continue, increment the round number and repeat
        round_number += 1


# This ensures main() runs only when executing this file directly:
# - It will NOT run if this file is imported into another Python file later.
if __name__ == "__main__":
    main()