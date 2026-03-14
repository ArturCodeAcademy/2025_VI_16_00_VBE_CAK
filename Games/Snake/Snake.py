import os
import random

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
    while new_position in snake_body:
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
                print(snake_head_char, end="")
            elif current_position in snake_body:
                print(snake_body_char, end="")
            elif current_position == food_position:
                print(food_char, end="")
            else:
                print(empty_cell_char, end="")
        print()


def get_user_input():
    # Use random input for testing purposes, replace with actual user input handling
    pass


def move_snake(new_head_position):
    # Move the snake by adding the new head position and removing the tail
    # Other parts must be updated accordingly
    pass


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
food_position = get_random_and_valid_position(snake_body, map_width, map_height)

snake_head_char = 'O'
snake_body_char = 'o'
food_char = '*'
empty_cell_char = '.'

show_map_and_stats()

# while not game_over:
    # show_map_and_stats()
    # direction = get_user_input()
    # new_head_position = add_positions(snake_body[0], direction)
    # check if new_head_position is valid and not colliding with snake_body
    # if valid:
        # move_snake(new_head_position)
    # else:
        # game_over = True

    # if food eaten increment score and place new food and grow snake
    # sleep for a short time to control game speed