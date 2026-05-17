class DayRunning:
    def __init__(self, day, duration):
        self.day = day
        self.duration = duration


runnings = []
min_duration = 24 * 60
with open("U1.txt", "r") as file:
    n = int(file.readline())
    for _ in range(n):
        values = list(map(int, file.readline().split()))
        day, msh, msm, meh, mem, esh, esm, eeh, eem = values

        if sum(values[1:5]) == 0 or sum(values[5:]) == 0:
            continue


        duration = (meh * 60 + mem - msh * 60 - msm) + (eeh * 60 + eem - esh * 60 - esm)
        day_running = DayRunning(day, duration)
        if duration < min_duration:
            min_duration = duration

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