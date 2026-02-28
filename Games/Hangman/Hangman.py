import os
import sys
import random


def print_colored_text(text):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']
    for c in text:
        color = random.choice(colors)
        print(f"{color}{c}\033[0m", end="")


def get_drawings():
    with open("Drawings.txt", "r") as file:
        return file.read().split("\n\n")


def get_answer():
    with open("Words.txt", "r") as file:
        words = file.read().split("\n")
        return random.choice(words)


def hide_word(word):
    hidden = ''
    for char in word:
        if char.isalpha():
            hidden += '_'
        else:
            hidden += char
    return hidden


def draw_used_letters(used_letters, hidden_word):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    green_color = '\033[92m'
    yellow_color = '\033[93m'
    red_color = '\033[91m'
    reset_color = '\033[0m'
    print(f"Used letters: ")
    for letter in alphabet:
        if letter in hidden_word.upper():
            print(f"{green_color}{letter}{reset_color} ", end="")
        elif letter in used_letters:
            print(f"{red_color}{letter.lower()}{reset_color} ", end="")
        else:
            print(f"{yellow_color}{letter}{reset_color} ", end="")
    print()


def draw_drawing(drawings, left_tries):
    back_ground = drawings[0].splitlines()
    foreground = drawings[left_tries].splitlines()
    foreground = (len(back_ground) - len(foreground)) * [' '] + foreground
    dark_gray_color = '\033[90m'
    red_color = '\033[91m'
    reset_color = '\033[0m'
    for bg_line, fg_line in zip(back_ground, foreground):
        length = max(len(bg_line), len(fg_line))
        for i in range(length):
            if i < len(fg_line) and fg_line[i] != ' ':
                print(f"{red_color}{fg_line[i]}{reset_color}", end="")
            else:
                print(f"{dark_gray_color}{bg_line[i]}{reset_color}", end="")
        print()

def draw_state(drawings, left_tries, hidden_word, used_letters):
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_drawing(drawings, left_tries)
    #print(drawings[left_tries])
    print('💜' * left_tries + '💔' * (total_tries - left_tries))
    print(f"Word: {hidden_word}")
    draw_used_letters(used_letters, hidden_word)


def get_user_input(used_letters):
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha() and guess not in used_letters:
            return guess

        print(f"Invalid input ({guess}). Please enter a single letter that you haven't used before.")


def open_letter_in_hidden_word(answer, hidden_word, guess):
    new_hidden = ''
    for i in range(len(answer)):
        if answer[i].upper() == guess:
            new_hidden += answer[i]
        else:
            new_hidden += hidden_word[i]
    return new_hidden


drawings = get_drawings()
total_tries = len(drawings) - 1
left_tries = total_tries
used_letters = ''
answer = get_answer()
hidden_word = hide_word(answer)

while left_tries > 0 and hidden_word != answer:
    draw_state(drawings, left_tries, hidden_word, used_letters)
    guess = get_user_input(used_letters)
    if guess in answer.upper():
        hidden_word = open_letter_in_hidden_word(answer, hidden_word, guess)
    else:
        left_tries -= 1
        used_letters = ''.join(sorted(used_letters + guess))

draw_state(drawings, left_tries, hidden_word, used_letters)
if hidden_word == answer:
    print_colored_text("Congratulations! ")
    print(f"You've guessed the word: {answer}")
else:
    print(f"Game Over! The correct word was: {answer}")

os.system("pause")