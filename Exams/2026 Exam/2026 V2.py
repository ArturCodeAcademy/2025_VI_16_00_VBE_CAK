class Answer:
    def __init__(self, team_name, question_name, time):
        self.team_name = team_name
        self.question_name = question_name
        self.time = time

class Team:
    def __init__(self, name):
        self.name = name
        self.total_time = 0
        self.solved_problems = 0


def sort_teams(teams):
    for i in range(len(teams) - 1):
        for j in range(i + 1, len(teams)):
            if (teams[i].solved_problems < teams[j].solved_problems) or \
               (teams[i].solved_problems == teams[j].solved_problems and teams[i].total_time > teams[j].total_time):
                teams[i], teams[j] = teams[j], teams[i]


def get_team_statistics(answers, team_name):
    team = Team(team_name)
    for answer in answers:
        if answer.team_name == team_name:
            team.total_time += answer.time
            team.solved_problems += 1
    return team


def get_questions_with_max_time(answers):
    max_time = 0
    result = []
    for answer in answers:
        if answer.time > max_time:
            max_time = answer.time
            result = [answer.question_name]
        elif answer.time == max_time and answer.question_name not in result:
            result.append(answer.question_name)

    return max_time, result


team_names = []
teams = []
answers = []

with open('Duomenys.txt') as file:
    question_count = int(file.readline())
    for _ in range(question_count):
        values = file.readline().strip().split()
        q_name, team_count = values[0], int(values[1])
        teams_values = values[2:]
        for i in range(0, len(teams_values), 2):
            team_name, time = teams_values[i], float(teams_values[i + 1])
            answer = Answer(team_name, q_name, time)
            answers.append(answer)

            if team_name not in team_names:
                team_names.append(team_name)

for team_name in team_names:
    team = get_team_statistics(answers, team_name)
    teams.append(team)

max_question_time, question_names = get_questions_with_max_time(answers)
sort_teams(teams)

with open('Rezultatai.txt', 'w') as file:
    file.write(f"{max_question_time:.1f}\n")
    first_found = False
    for q in question_names:
        if first_found:
            file.write(" ")
        file.write(f"{q}")
        first_found = True
    file.write("\n")
    for team in teams:
        file.write(f"{team.name} {team.solved_problems} {team.total_time:.1f}\n")