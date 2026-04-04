def find_max_value():
    with open("U1.txt", "r") as file:
        return max(map(int, file.read().split()[1:]))

def find_count_of_values_twice_smaller_than_max(max_value):
    with open("U1.txt", "r") as file:
        return len([1 for line in file.read().split()[1:] if int(line.strip()) * 2 <= max_value])

with open("U1rez.txt", "w") as output_file:
    output_file.write(f"{find_max_value()} {find_count_of_values_twice_smaller_than_max(find_max_value())}")
    