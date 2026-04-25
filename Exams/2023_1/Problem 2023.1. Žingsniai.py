class Participant:
    def __init__(self, group, step_length, steps):
        self.group = group
        self.step_length = step_length
        self.steps = steps
        self.valid_data = 0 not in steps
        self.distance = step_length * sum(steps) / 100000


class Group:
    def __init__(self, id):
        self.id = id
        self.participants_count = 0
        self.total_distance = 0