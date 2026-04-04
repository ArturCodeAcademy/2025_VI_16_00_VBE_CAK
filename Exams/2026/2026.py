class Student:
    def __init__(self, fullname, id, class_name):
        self.fullname = fullname
        self.id = id
        self.class_name = class_name

    def __str__(self):
        return f"{self.fullname} {self.id} {self.class_name}"


class StudentsSubjects:
    def __init__(self, id, subjects):
        self.id = id
        self.subjects = subjects

    def __str__(self):
        return f"{self.id} {self.subjects}"


class SubjectStatistics:
    def __init__(self, subject_name, students_count):
        self.subject_name = subject_name
        self.students_count = students_count

    def __str__(self):
        return f"{self.subject_name} {self.students_count}"


def calculate_students_in_class(students, class_name):
    s = 0
    for student in students:
        if student.class_name == class_name:
            s += 1
    return s


def calculate_id_digits_sum(id):
    digits = id[-4:]
    if not digits.isdigit():
        return False

    return sum(map(int, digits))


def is_id_valid(id):
    return calculate_id_digits_sum(id) == 15


def is_id_valid2(id):
    digits = id[-4:]
    if not digits.isdigit():
        return False

    s = 0
    for digit in digits:
        s += int(digit)

    if s == 15:
        return True
    else:
        return False


def get_students_with_incorrect_ids(students):
    new_arr = []
    for student in students:
        if not is_id_valid(student.id):
            new_arr.append(student)

    return new_arr


def is_student_selected_subjects_correctly(student, subjects):
    for subject in subjects:
        if student.id == subject.id:
            if 3 <= len(subject.subjects) <= 7 and "BL" in subject.subjects and "MAT" in subject.subjects:
                return True
            else:
                return False

    return True


students = []
subjects = []

with open("Duomenys.txt", "r") as fin:
    students_count = int(fin.readline())

    for _ in range(students_count):
        name, id, class_name = fin.readline().strip().split(';')
        student = Student(name, id, class_name)
        students.append(student)

    for line in fin:
        values = line.strip().split(';')
        id, *subs = values
        subject = StudentsSubjects(id, subs)
        subjects.append(subject)

# Check input
print("\n".join(map(str, students)))
print()
print("\n".join(map(str, subjects)))
print()

a12 = calculate_students_in_class(students, "12a")
b12 = calculate_students_in_class(students, "12b")
c12 = calculate_students_in_class(students, "12c")

students_with_incorrect_ids = get_students_with_incorrect_ids(students)

subjects_statistics = []
for students_subjects in subjects:
    for subject in students_subjects.subjects:
        found = False
        for stat in subjects_statistics:
            if stat.subject_name == subject:
                stat.students_count += 1
                found = True
                break

        if not found:
            subjects_statistics.append(SubjectStatistics(subject, 1))

# subjects_statistics.sort(key=lambda x: (-x.students_count, x.subject_name))

for i in range(len(subjects_statistics) - 1):
    for j in range(i + 1, len(subjects_statistics)):
        if subjects_statistics[i].students_count < subjects_statistics[j].students_count:
            subjects_statistics[i], subjects_statistics[j] = subjects_statistics[j], subjects_statistics[i]
        elif subjects_statistics[i].students_count == subjects_statistics[j].students_count:
            if subjects_statistics[i].subject_name > subjects_statistics[j].subject_name:
                subjects_statistics[i], subjects_statistics[j] = subjects_statistics[j], subjects_statistics[i]

with open("Rezultatai.txt", "w") as fout:
    fout.write(f"{a12} {b12} {c12}\n")
    fout.write(f"{len(students_with_incorrect_ids)}\n")
    for student in students_with_incorrect_ids:
        fout.write(f"{student.fullname} {student.id} {calculate_id_digits_sum(student.id)}\n")
    for student in students:
        if not is_student_selected_subjects_correctly(student, subjects):
            fout.write(f"{student.fullname}\n")

    for stat in subjects_statistics:
        fout.write(str(stat))
        fout.write("\n")
