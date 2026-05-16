class Student:
    def __init__(self, name):
        self.name = name
        self.total_hours = 0


class Activity:
    def __init__(self, name):
        self.name = name
        self.hours = 0


def sort_students(students):
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if students[i].name > students[j].name:
                students[i], students[j] = students[j], students[i]


def sort_activities(activities):
    for i in range(len(activities)):
        for j in range(i + 1, len(activities)):
            if activities[i].hours < activities[j].hours:
                activities[i], activities[j] = activities[j], activities[i]

students = []
activities = []
total_hours = 0

with open("Duomenys.txt", "r") as file:
    student_count = int(file.readline().strip())
    for _ in range(student_count):
        name, activity_count = file.readline().strip().split()
        activity_count = int(activity_count)
        student = Student(name)
        for _ in range(activity_count):
            activity_name, *hours = file.readline().split()
            hours = list(map(int, hours[1:]))
            student.total_hours += sum(hours)
            total_hours += sum(hours)

            for activity in activities:
                if activity.name == activity_name:
                    activity.hours += sum(hours)
                    break
            else:
                new_activity = Activity(activity_name)
                new_activity.hours = sum(hours)
                activities.append(new_activity)

        students.append(student)

sort_students(students)
sort_activities(activities)

with open("Rezultatai.txt", "w") as file:
    file.write("Statistika\n")
    for activity in activities:
        file.write(f"{activity.name} {activity.hours / total_hours * 100:.2f} %\n")

    file.write("Mokiniai\n")
    for student in students:
        if student.total_hours >= 20:
            file.write(f"{student.name} {student.total_hours}\n")