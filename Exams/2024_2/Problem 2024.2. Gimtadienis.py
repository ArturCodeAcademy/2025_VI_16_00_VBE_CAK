class AvailableTime:
    def __init__(self, day, time):
        self.day = day
        self.time = time
        self.friends = []

    def __str__(self):
        if len(self.friends) == 0:
            return f"{self.day:<3} {self.time} {len(self.friends)}"
        else:
            return f"{self.day:<3} {self.time} {len(self.friends)}\n" + '\n'.join(self.friends)


def sort_times(times):
    for i in range(len(times) - 1):
        for j in range(i + 1, len(times)):
            if len(times[i].friends) < len(times[j].friends):
                times[i], times[j] = times[j], times[i]

available_times = []
with open("U2.txt", "r") as fin:
    n, m = map(int, fin.readline().split())
    for _ in range(n):
        day, *times = fin.readline().split()
        for time in map(int, times[1:]):
            available_times.append(AvailableTime(day, time))

    for _ in range(m):
        line = fin.readline().strip()
        name = line[:12]
        values = line[12:].split()[1:]
        for i in range(0, len(values), 2):
            day = values[i]
            time = int(values[i + 1])
            for t in available_times:
                if t.day == day and t.time == time:
                    t.friends.append(name)
                    break

sort_times(available_times)

with open("U2rez.txt", "w") as fout:
    for t in available_times:
        if len(t.friends) < 4:
            break

        t.friends.sort()
        fout.write(str(t))
        fout.write("\n")