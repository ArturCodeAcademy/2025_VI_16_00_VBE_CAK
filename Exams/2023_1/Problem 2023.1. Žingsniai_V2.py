a = [(group_id, step_length * sum(steps) / 100000) for group_id, step_length, *steps in [list(map(int, line.split())) for line in open("U1.txt", "r").readlines()[1:]] if 0 not in steps]
open("U1rez.txt", "w").write("\n".join([f"{id} {sum(1 for x in a if x[0] == id)} {sum(x[1] for x in a if x[0] == id):.02f}" for i, (id, dist) in enumerate(a)if i == list(map(lambda x: x[0], a)).index(id)]))
