import os
import datetime

game_board = [' '] * 9
current_player = 'X'
player_1_turn = True
winner = ""
game_ended = False

player_1_name = input("Enter name for Player 1 (X): ")
player_2_name = input("Enter name for Player 2 (O): ")

start_timer = datetime.datetime.now()

if player_1_name.strip() == "":
    player_1_name = "Player 1"
if player_2_name.strip() == "":
    player_2_name = "Player 2"

log_file_path = os.path.join("GameLogs", f"{datetime.datetime.now():%Y%m%d_%H%M%S}.log")
os.makedirs("GameLogs", exist_ok=True)
log_file = open(log_file_path, 'w', encoding='utf-8')

log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Game started between {player_1_name} (X) and {player_2_name} (O)\n")

while not game_ended:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Current board:")
    for i in range(3):
        print(f" {game_board[i*3]} | {game_board[i*3+1]} | {game_board[i*3+2]} ")
        if i < 2:
            print("---+---+---")

    if player_1_turn:
        current_player = player_1_name
        current_player_symbol = 'X'
        log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {player_1_name}'s (X) turn\n")
    else:
        current_player = player_2_name
        current_player_symbol = 'O'
        log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {player_2_name}'s (O) turn\n")

    print(f"\n{current_player}'s ({current_player_symbol}) turn. Available positions:")
    for i in range(3):
        for j in range(3):
            idx = i * 3 + j
            if game_board[idx] == ' ':
                print(f" {idx}", end='')
            else:
                print("  ", end='')

            if j < 2:
                print(" |", end='')

        if i < 2:
            print("\n---+---+---")
        else:
            print()

    while True:
        choice = input(f"\nSelect a position (0-8) for {current_player} ({current_player_symbol}): ")
        log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {current_player} selected position {choice}\n")
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 0 and 8 from the available positions.")
            continue

        choice = int(choice)
        if choice < 0 or choice > 8:
            print("Invalid input. Please enter a number between 0 and 8.")
            continue

        if game_board[choice] != ' ':
            print("Position already taken. Choose another position.")
            continue

        break

    if player_1_turn:
        game_board[choice] = 'X'
    else:
        game_board[choice] = 'O'

    log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Board state: {game_board}\n")

    if game_board[0] == game_board[4] == game_board[8] != ' ':
        winner = game_board[0]
        log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Winner detected: {winner} (main diagonal)\n")
    elif game_board[2] == game_board[4] == game_board[6] != ' ':
        winner = game_board[2]
        log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Winner detected: {winner} (anti diagonal)\n")
    for i in range(3):
        if game_board[i*3] == game_board[i*3 + 1] == game_board[i*3 + 2] != ' ':
            winner = game_board[i*3]
            log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Winner detected: {winner} (row {i + 1})\n")
            break

        if game_board[i] == game_board[i + 3] == game_board[i + 6] != ' ':
            winner = game_board[i]
            log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Winner detected: {winner} (column {i + 1})\n")
            break

    if winner != "":
        game_ended = True
        break

    if ' ' not in game_board and winner == "":
        game_ended = True
        log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Game ended in a draw\n")
        break

    player_1_turn = not player_1_turn
    log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Next turn\n")

os.system('cls' if os.name == 'nt' else 'clear')
print(f"Final board:")
for i in range(3):
    print(f" {game_board[i*3]} | {game_board[i*3+1]} | {game_board[i*3+2]} ")
    if i < 2:
        print("---+---+---")

winner_name = ""
if winner == 'X':
    winner_name = player_1_name
elif winner == 'O':
    winner_name = player_2_name

if winner_name != "":
    print(f"\nCongratulations {winner_name}! You have won the game!")
    log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {winner_name} has won the game\n")
else:
    print("\nThe game is a draw!")
    log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] The game ended in a draw\n")

end_timer = datetime.datetime.now()
duration = end_timer - start_timer
log_file.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Game duration: {duration}\n")

log_file.close()