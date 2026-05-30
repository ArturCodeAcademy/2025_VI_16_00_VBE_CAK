class Subject:
    def __init__(self, name):
        self.name = name
        self.students = []


def sort_by_count(subjects):
    for i in range(len(subjects)):
        for j in range(i + 1, len(subjects)):
            if len(subjects[i].students) < len(subjects[j].students) or len(subjects[i].students) == len(subjects[j].students) and subjects[i].name > subjects[j].name:
                    subjects[i], subjects[j] = subjects[j], subjects[i]


subjects = []
with open("U2.txt", "r") as file:
    n = int(file.readline())
    for line in file:
        name, subject, grade_count, *grades = line.split()
        grade_count = int(grade_count)
        grades = list(map(int, grades))
        avg = sum(grades) / grade_count
        if avg >= 9:
            for sub in subjects:
                if sub.name == subject:
                    sub.students.append(name)
                    break
            else:
                s = Subject(subject)
                s.students.append(name)
                subjects.append(s)

sort_by_count(subjects)
with open("U2rez.txt", "w") as file:
    if len(subjects) == 0:
        file.write("Neatitinka vidurkis")
    else:
        for subject in subjects:
            file.write(subject.name + " " + str(len(subject.students)) + "\n")
            for student in subject.students:
                file.write(student + "\n")