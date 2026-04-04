def find_max_value():
    with open("U1.txt", "r") as file:
        max_value = None
        file.readline()
        for line in file:
            value = int(line.strip())
            if max_value is None or value > max_value:
                max_value = value
        return max_value

def find_count_of_values_twice_smaller_than_max(max_value):
    with open("U1.txt", "r") as file:
        count = 0
        file.readline()
        for line in file:
            value = int(line.strip())
            if value * 2 <= max_value:
                count += 1
        return count

m = find_max_value()
c = find_count_of_values_twice_smaller_than_max(m)

with open("U1rez.txt", "w") as output_file:
    output_file.write(f"{m} {c}")