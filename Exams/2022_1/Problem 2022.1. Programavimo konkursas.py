class Participant:
    def __init__(self, name, task_time):
        self.name = name
        self.task_time = task_time
        self.score = 0
        self.spent_time = 0
        self.tasks_solved = 0

    def __str__(self):
        return f"{self.name} {self.task_time} {self.score} {self.spent_time} {self.tasks_solved}"

def calculate_participant_data(participant, time_limits, task_points):
    for i in range(len(participant.task_time)):
        if participant.task_time[i] == 0:
            continue

        if participant.task_time[i] <= time_limits[i]:
            participant.score += task_points[i]
        else:
            participant.score += task_points[i] // 2

        participant.spent_time += participant.task_time[i]
        participant.tasks_solved += 1

def sort_participants(participants):
    for i in range(len(participants)):
        for j in range(i + 1, len(participants)):
            if participants[i].tasks_solved < participants[j].tasks_solved:
                participants[i], participants[j] = participants[j], participants[i]

def sort_participants2(participants):
    participants.sort(key=lambda p: -p.tasks_solved)

participants = []
with open("U1.txt", "r") as fin:
    fin.readline()
    time_limits = list(map(int, fin.readline().split()))
    task_points = list(map(int, fin.readline().split()))
    for line in fin:
        name = line[:10]
        spent_times = list(map(int, line[10:].split()))
        participant = Participant(name, spent_times)
        participants.append(participant)

best_score = 0
for participant in participants:
    calculate_participant_data(participant, time_limits, task_points)
    if participant.score > best_score:
        best_score = participant.score

sort_participants2(participants)

with open("U1rez.txt", "w") as fout:
    fout.write(f"{best_score}\n")
    for p in participants:
        if p.score == best_score:
            fout.write(f"{p.name} {p.tasks_solved} {p.spent_time}\n")
