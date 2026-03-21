import os
import random
import time
import keyboard


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f"({self.x}, {self.y})"


    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False


def add_positions(pos1, pos2):
    return Position(pos1.x + pos2.x, pos1.y + pos2.y)


def is_position_valid(position, map_width, map_height):
    return 0 <= position.x < map_width and 0 <= position.y < map_height


def get_random_and_valid_position(snake_body, map_width, map_height):
    new_position = Position(random.randint(0, map_width - 1),
                            random.randint(0, map_height - 1))
    while new_position in snake_body or new_position in food_positions:
        new_position = Position(random.randint(0, map_width - 1),
                                random.randint(0, map_height - 1))
    return new_position


def initialize_snake(head, initial_length, direction):
    new_snake_body = [head]
    direction = Position(-direction.x, -direction.y)  # Reverse direction to build the body
    for _ in range(1, initial_length):
        new_body_part = add_positions(new_snake_body[-1], direction)
        new_snake_body.append(new_body_part)
    return new_snake_body



def show_map_and_stats():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Snake Length: {len(snake_body)}")

    for y in range(map_height):
        for x in range(map_width):
            current_position = Position(x, y)
            if current_position == snake_body[0]:
                print(snake_head_color + snake_head_char + RESET, end="")
            elif current_position in snake_body:
                print(snake_body_color + snake_body_char + RESET, end="")
            elif current_position in food_positions:
                print(food_color + food_char + RESET, end="")
            else:
                print(empty_cell_color + empty_cell_char + RESET, end="")
        print()


def get_random_input(last_direction):
    choice = random.randint(1, 4)
    if choice == 1:
        new_direction =  UP
    elif choice == 2:
        new_direction =  DOWN
    elif choice == 3:
        new_direction =  LEFT
    else:
        new_direction =  RIGHT

    if add_positions(new_direction, last_direction) == Position(0, 0):
        return last_direction
    return new_direction


def get_user_input(last_direction):
    choice = random.randint(1, 4)
    if keyboard.is_pressed('up'):
        new_direction =  UP
    elif keyboard.is_pressed('down'):
        new_direction =  DOWN
    elif keyboard.is_pressed('left'):
        new_direction =  LEFT
    elif keyboard.is_pressed('right'):
        new_direction =  RIGHT
    else:
        new_direction = last_direction

    if add_positions(new_direction, last_direction) == Position(0, 0):
        return last_direction
    return new_direction


def move_snake(new_head_position):
    snake_body.insert(0, new_head_position)  # Add new head
    snake_body.pop()  # Remove tail (unless we eat food, then we won't pop)


def game_over_animation():
    snake_length = len(snake_body)
    dead_char = 'X'
    dead_color = MAGENTA
    pause_duration = 2 / snake_length  # Faster animation for longer snakes

    dead_body = []
    for i in range(snake_length + 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Snake Length: {snake_length}")

        for y in range(map_height):
            for x in range(map_width):
                current_position = Position(x, y)
                if current_position in dead_body:
                    print(dead_color + dead_char + RESET, end="")
                elif current_position == snake_body[0]:
                    print(snake_head_color + snake_head_char + RESET, end="")
                elif current_position in snake_body:
                    print(snake_body_color + snake_body_char + RESET, end="")
                else:
                    print(empty_cell_color + empty_cell_char + RESET, end="")
            print()

        if i < snake_length:
            dead_body.append(snake_body[snake_length - 1 - i])
        time.sleep(pause_duration)

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'


# Directions as positions
UP = Position(0, -1)
DOWN = Position(0, 1)
LEFT = Position(-1, 0)
RIGHT = Position(1, 0)

initial_length = 3
map_width = 20
map_height = 10

center_position = Position(map_width // 2, map_height // 2)
initial_direction = RIGHT
snake_body = initialize_snake(center_position, initial_length, initial_direction)
food_count = 5
food_positions = []
food_positions = [get_random_and_valid_position(snake_body, map_width, map_height) for _ in range(food_count)]
pause_duration = 0.2

snake_head_char = 'O'
snake_body_char = 'o'
food_char = '*'
empty_cell_char = '.'

snake_head_color = GREEN
snake_body_color = YELLOW
food_color = RED
empty_cell_color = BLUE

game_over = False
last_direction = initial_direction
direction = initial_direction
next_draw_time = time.time() + pause_duration

while not game_over:
    show_map_and_stats()
    while time.time() < next_draw_time:
        direction = get_user_input(last_direction)
    next_draw_time = time.time() + pause_duration
    new_head_position = add_positions(snake_body[0], direction)
    if is_position_valid(new_head_position, map_width, map_height) and new_head_position not in snake_body:
        move_snake(new_head_position)
        if new_head_position in food_positions:
            food_positions.remove(new_head_position)
            food_position = get_random_and_valid_position(snake_body, map_width, map_height)
            food_positions.append(food_position)
            snake_body.append(snake_body[-1])  # Grow snake by adding a new tail segment
    else:
        game_over = True

    last_direction = direction

game_over_animation()
print("Game Over! Final Length:", len(snake_body))