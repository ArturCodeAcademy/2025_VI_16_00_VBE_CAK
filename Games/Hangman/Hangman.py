import os
import sys
import random


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


def draw_state(drawings, left_tries, hidden_word, used_letters):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(drawings[left_tries])
    print(f"Word: {hidden_word}")
    print(f"Used letters: {used_letters}")


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
    print(f"Congratulations! You've guessed the word: {answer}")
else:
    print(f"Game Over! The correct word was: {answer}")

os.system("pause")