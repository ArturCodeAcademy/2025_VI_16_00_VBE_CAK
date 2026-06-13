class Team:
    def __init__(self, name):
        self.name = name
        self.total_time = 0
        self.solved_problems = 0


class Question:
    def __init__(self, name):
        self.name = name
        self.max_time = 0


def find_team_by_name(teams, name):
    for team in teams:
        if team.name == name:
            return team
    return None


def sort_teams(teams):
    for i in range(len(teams) - 1):
        for j in range(i + 1, len(teams)):
            if (teams[i].solved_problems < teams[j].solved_problems) or \
               (teams[i].solved_problems == teams[j].solved_problems and teams[i].total_time > teams[j].total_time):
                teams[i], teams[j] = teams[j], teams[i]

teams = []
questions = []
max_question_time = 0

with open('Duomenys.txt') as file:
    question_count = int(file.readline())
    for _ in range(question_count):
        values = file.readline().strip().split()
        q_name, team_count = values[0], int(values[1])
        question = Question(q_name)
        teams_values = values[2:]
        for i in range(0, len(teams_values), 2):
            team_name, time = teams_values[i], float(teams_values[i + 1])
            team = find_team_by_name(teams, team_name)
            if team is None:
                team = Team(team_name)
                teams.append(team)
            team.solved_problems += 1
            team.total_time += time
            if time > question.max_time:
                question.max_time = time
                if time > max_question_time:
                    max_question_time = time
        questions.append(question)

sort_teams(teams)

with open('Rezultatai.txt', 'w') as file:
    file.write(f"{max_question_time:.1f}\n")
    first_found = False
    for q in questions:
        if q.max_time == max_question_time:
            if first_found:
                file.write(" ")
            file.write(f"{q.name}")
            first_found = True
    file.write("\n")
    for team in teams:
        file.write(f"{team.name} {team.solved_problems} {team.total_time:.1f}\n")