import random

def play_game():
    difficulties = {
        "1": ("Easy",   1,  50,  8),
        "2": ("Medium", 1, 100, 10),
        "3": ("Hard",   1, 200, 12),
    }

    print("\n=== NUMBER GUESSING GAME ===")
    print("1. Easy   (1–50,  8 guesses)")
    print("2. Medium (1–100, 10 guesses)")
    print("3. Hard   (1–200, 12 guesses)")

    while True:
        choice = input("\nChoose difficulty (1/2/3): ").strip()
        if choice in difficulties:
            break
        print("Please enter 1, 2, or 3.")

    name, lo, hi, max_attempts = difficulties[choice]
    secret = random.randint(lo, hi)
    guesses = []

    print(f"\n[{name}] I've picked a number between {lo} and {hi}.")
    print(f"You have {max_attempts} guesses. Good luck!\n")

    for attempt in range(1, max_attempts + 1):
        remaining = max_attempts - attempt + 1
        while True:
            try:
                guess = int(input(f"Guess {attempt}/{max_attempts} (range {lo}–{hi}): "))
                if lo <= guess <= hi:
                    break
                print(f"  Enter a number between {lo} and {hi}.")
            except ValueError:
                print("  Please enter a valid integer.")

        guesses.append(guess)

        if guess == secret:
            print(f"\n  Correct! The number was {secret}.")
            print(f"  Solved in {attempt} guess{'es' if attempt > 1 else ''}!")
            print(f"  Your guesses: {guesses}")
            return True
        elif guess < secret:
            lo = max(lo, guess + 1)
            print(f"  Too low  ↑  (narrowed range: {lo}–{hi}, {remaining - 1} left)")
        else:
            hi = min(hi, guess - 1)
            print(f"  Too high ↓  (narrowed range: {lo}–{hi}, {remaining - 1} left)")

    print(f"\n  Out of guesses! The number was {secret}.")
    print(f"  Your guesses: {guesses}")
    return False

def main():
    wins, total = 0, 0
    while True:
        total += 1
        if play_game():
            wins += 1
        print(f"\nRecord: {wins} win{'s' if wins != 1 else ''} / {total} game{'s' if total != 1 else ''}")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print(f"\nFinal score: {wins}/{total}. Thanks for playing!")
            break

if __name__ == "__main__":
    main()
