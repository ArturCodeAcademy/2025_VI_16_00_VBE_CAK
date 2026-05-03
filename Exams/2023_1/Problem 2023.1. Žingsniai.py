class Participant:
    def __init__(self, group, step_length, steps):
        self.group = group
        self.step_length = step_length
        self.steps = steps
        self.valid_data = 0 not in steps
        self.distance = step_length * sum(steps) / 100000


    def __str__(self):
        return f"Group: {self.group}, Step Length: {self.step_length}, Steps: {self.steps}, Distance: {self.distance:.2f} km, Valid Data: {self.valid_data}"


class Group:
    def __init__(self, id):
        self.id = id
        self.participants_count = 0
        self.total_distance = 0


participants = []
groups = []
with open("U1.txt", "r") as file:
    file.readline()
    for line in file:
        values = list(map(int, line.split()))
        group_id, step_length, *steps = values
        participant = Participant(group_id, step_length, steps)
        participants.append(participant)

for participant in participants:
    if not participant.valid_data:
        continue

    group_exists = False
    for group in groups:
        if group.id == participant.group:
            group.participants_count += 1
            group.total_distance += participant.distance
            group_exists = True
            break

    if not group_exists:
        new_group = Group(participant.group)
        new_group.participants_count = 1
        new_group.total_distance = participant.distance
        groups.append(new_group)


with open("U1rez.txt", "w") as file:
    for group in groups:
        file.write(f"{group.id} {group.participants_count} {group.total_distance:.2f}\n")