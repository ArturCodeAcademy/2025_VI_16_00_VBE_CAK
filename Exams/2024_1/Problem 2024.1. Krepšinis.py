class Participant:
    def __init__(self, id, penalty_hit, penalty_thrown, double_hit, double_thrown, triple_hit, triple_thrown):
        self.id = id
        self.penalty_hit = penalty_hit
        self.penalty_thrown = penalty_thrown
        self.double_hit = double_hit
        self.double_thrown = double_thrown
        self.triple_hit = triple_hit
        self.triple_thrown = triple_thrown
        self.total_points = penalty_hit + double_hit * 2 + triple_hit * 3
        self.accuracy = (penalty_hit + double_hit + triple_hit) / (penalty_thrown + double_thrown + triple_thrown) * 100
        self.games_played = 1


def find_player_index(participants, id):
    for i, participant in enumerate(participants):
        if participant.id == id:
            return i
    return -1


with open("U1.txt", "r") as fin:
    n = int(fin.readline())
    participants = []
    max_games_played = 1

    for _ in range(n):
        values = list(map(int, fin.readline().split()))
        id = values[0]
        index = find_player_index(participants, id)
        if index == -1:
            participant = Participant(*values)
            participants.append(participant)
        else:
            participants[index].penalty_hit += values[1]
            participants[index].penalty_thrown += values[2]
            participants[index].double_hit += values[3]
            participants[index].double_thrown += values[4]
            participants[index].triple_hit += values[5]
            participants[index].triple_thrown += values[6]
            participants[index].total_points += values[1] + values[3] * 2 + values[5] * 3
            participants[index].accuracy = (participants[index].penalty_hit + participants[index].double_hit + participants[index].triple_hit) / (participants[index].penalty_thrown + participants[index].double_thrown + participants[index].triple_thrown) * 100
            participants[index].games_played += 1
            if participants[index].games_played > max_games_played:
                max_games_played = participants[index].games_played

with open("U1rez.txt", "w") as fout:
    fout.write(f"{max_games_played}\n")
    for participant in participants:
        if participant.games_played == max_games_played:
            fout.write(f"{participant.id} {participant.total_points / max_games_played:.1f} {participant.accuracy:.0f} %\n")