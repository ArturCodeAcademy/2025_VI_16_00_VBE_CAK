import random


# ---------- COLORS ----------
RED = '\033[91m'
DARK_RED = '\033[31m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
PURPLE = '\033[95m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'


# ---------- SYMBOLS ----------
HEART = '❤'
BROKEN_HEART = '💔'
STAR = '★'
FIRE = '🔥'
TARGET = '🎯'


# ---------- SETTINGS ----------
MIN_NUMBER = 1
MAX_NUMBER = 1000
MAX_LIVES = 10


def color_text(text, color):
    return color + str(text) + RESET


def print_line():
    print(color_text("-" * 45, PURPLE))


def print_intro():
    print_line()
    print(color_text("Welcome to the Number Guesser Game!", BOLD + CYAN))
    print(color_text(f"I have chosen a number from {MIN_NUMBER} to {MAX_NUMBER}.", YELLOW))
    print(color_text(f"You have {MAX_LIVES} lives. Try to guess it!", GREEN))
    print_line()


def print_lives(lives):
    hearts = RED + HEART * lives + RESET
    broken_hearts = DARK_RED + BROKEN_HEART * (MAX_LIVES - lives) + RESET

    print(color_text("Lives: ", BOLD + WHITE) + hearts + broken_hearts)


def print_range(min_value, max_value):
    if min_value == max_value:
        print(color_text(f"Range: [ {min_value} ]", BLUE))
    else:
        print(color_text(f"Range: [ {min_value} ... {max_value} ]", BLUE))


def get_guess():
    try:
        guess = int(input(color_text("Enter your guess: ", BOLD + CYAN)))
        return guess
    except ValueError:
        print(color_text("Please enter a valid number!", RED))
        return None


def is_guess_valid(guess):
    if guess < MIN_NUMBER or guess > MAX_NUMBER:
        print(color_text(f"Your guess must be between {MIN_NUMBER} and {MAX_NUMBER}!", RED))
        return False

    return True


def check_guess(guess, secret_number):
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "low"
    else:
        return "high"


def print_win(secret_number, guess_count, lives):
    print()
    print_line()
    print(color_text(f"{STAR} Congratulations! You guessed the number! {STAR}", BOLD + GREEN))
    print(color_text(f"The number was {secret_number}.", YELLOW))
    print(color_text(f"You needed {guess_count} guesses.", CYAN))
    print(color_text(f"Lives left: {lives}", GREEN))
    print_line()


def print_game_over(secret_number):
    print()
    print_line()
    print(DARK_RED + BROKEN_HEART * MAX_LIVES + RESET)
    print(color_text("Game over!", BOLD + RED))
    print(color_text(f"The correct number was {secret_number}.", YELLOW))
    print_line()


def play_game():
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    guess_count = 0
    lives = MAX_LIVES

    min_range_value = MIN_NUMBER
    max_range_value = MAX_NUMBER

    print_intro()

    while lives > 0:
        print()
        print_lives(lives)
        print_range(min_range_value, max_range_value)

        guess = get_guess()

        if guess is None:
            continue

        if not is_guess_valid(guess):
            continue

        guess_count += 1

        result = check_guess(guess, secret_number)

        if result == "correct":
            print_win(secret_number, guess_count, lives)
            break

        elif result == "low":
            print(color_text("Too low!", YELLOW))
            print(color_text(f"{TARGET} Try a bigger number!", CYAN))
            lives -= 1
            min_range_value = max(min_range_value, guess + 1)

        elif result == "high":
            print(color_text("Too high!", PURPLE))
            print(color_text(f"{FIRE} Try a smaller number!", CYAN))
            lives -= 1
            max_range_value = min(max_range_value, guess - 1)

    if lives == 0:
        print_game_over(secret_number)


play_game()