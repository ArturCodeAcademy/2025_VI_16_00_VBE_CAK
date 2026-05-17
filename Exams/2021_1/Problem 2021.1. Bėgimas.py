class DayRunning:
    def __init__(self, day, morning_time, evening_time):
        self.day = day
        self.morning_time = morning_time
        self.evening_time = evening_time
        self.duration = morning_time.duration + evening_time.duration


class RunningTime:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = (end_time.hours * 60 + end_time.minutes
                         - start_time.hours * 60 - start_time.minutes)


    def __str__(self):
        return f"{self.start_time.hours}:{self.start_time.minutes} - {self.end_time.hours}:{self.end_time.minutes} ({self.duration} min)"


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes


runnings = []
min_duration = 24 * 60
with open("U1.txt", "r") as file:
    n = int(file.readline())
    for _ in range(n):
        values = list(map(int, file.readline().split()))
        day, msh, msm, meh, mem, esh, esm, eeh, eem = values

        if sum(values[1:5]) == 0 or sum(values[5:]) == 0:
            continue

        morning_start_time = Time(msh, msm)
        morning_end_time = Time(meh, mem)
        evening_start_time = Time(esh, esm)
        evening_end_time = Time(eeh, eem)

        morning_running = RunningTime(morning_start_time, morning_end_time)
        evening_running = RunningTime(evening_start_time, evening_end_time)

        day_running = DayRunning(day, morning_running, evening_running)
        if day_running.duration < min_duration:
            min_duration = day_running.duration

        runnings.append(day_running)

first_day_found = False
with open("U1rez.txt", "w") as file:
    file.write(f"Minimalus laikas\n")
    file.write(f"{min_duration}\n")
    file.write(f"Dienos\n")
    for running in runnings:
        if running.duration == min_duration:
            if first_day_found:
                file.write(" ")
            file.write(f"{running.day}")
            first_day_found = True