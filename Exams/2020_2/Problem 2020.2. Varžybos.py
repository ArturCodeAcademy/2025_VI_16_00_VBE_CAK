class Participant:
    def __init__(self, name, fish):
        self.name = name
        self.fish = fish
        self.total_score = 0


class FishPoints:
    def __init__(self, name, points):
        self.name = name
        self.points = points


class FishWeight:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.points = 0


def sort_fish_by_points_desc(fish):
    for i in range(len(fish) - 1):
        for j in range(len(fish) - i - 1):
            if fish[j].points < fish[j + 1].points:
                fish[j], fish[j + 1] = fish[j + 1], fish[j]


def sort_participants_by_points_desc(participants):
    for i in range(len(participants) - 1):
        for j in range(len(participants) - i - 1):
            if participants[j].total_score < participants[j + 1].total_score or (participants[j].total_score == participants[j + 1].total_score and participants[j].name > participants[j + 1].name):
                participants[j], participants[j + 1] = participants[j + 1], participants[j]


def sort_fish_weights_by_points_desc(fish_points):
    for i in range(len(fish_points) - 1):
        for j in range(len(fish_points) - i - 1):
            if fish_points[j].weight < fish_points[j + 1].weight or (fish_points[j].weight == fish_points[j + 1].weight and fish_points[j].name > fish_points[j + 1].name):
                fish_points[j], fish_points[j + 1] = fish_points[j + 1], fish_points[j]


participants = []
fish_points = []
fish_weights = []

with open("U2.txt", "r") as file:
    participants_count = int(file.readline().strip())
    for _ in range(participants_count):
        line = file.readline()
        name = line[:20]
        fish_count = int(line[20:])
        fish = []
        for _ in range(fish_count):
            line = file.readline()
            fish_name = line[:20]
            fish_weight = int(line[20:])
            f = FishWeight(fish_name, fish_weight)
            fish.append(f)
        p = Participant(name, fish)
        participants.append(p)

    fish_count = int(file.readline())
    for _ in range(fish_count):
        line = file.readline()
        fish_name = line[:20]
        fish_points_value = int(line[20:])
        fp = FishPoints(fish_name, fish_points_value)
        fish_points.append(fp)
        fw = FishWeight(fish_name, 0)
        fish_weights.append(fw)

for p in participants:
    for f in p.fish:
        for fp in fish_points:
            if fp.name == f.name:
                f.points = fp.points
                if f.weight >= 200:
                    f.points += 30
                else:
                    f.points += 10

        for fw in fish_weights:
            if fw.name == f.name:
                fw.weight += f.weight
                break

    sort_fish_by_points_desc(p.fish)

    for i in range(min(5, len(p.fish))):
        p.total_score += p.fish[i].points

sort_participants_by_points_desc(participants)
sort_fish_weights_by_points_desc(fish_weights)

with open("U2rez.txt", "w") as file:
    file.write(f"Dalyviai\n")
    for p in participants:
        file.write(f"{p.name} {p.total_score}\n")

    file.write(f"Laimikis\n")
    for fw in fish_weights:
        file.write(f"{fw.name} {fw.weight}\n")