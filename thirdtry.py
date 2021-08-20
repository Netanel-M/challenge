
dataset = {
    "foo": ["bar", "baz"],
    "orange": ["bnanana", "mango"],
    "bar": ["qux", "quux"],
    "monkey": ["cow", "parrot"],
    "mango": ["banana"],
    "baz": ["spam"],
    "spam": ["mango"],
    "banana": ["baz"],
    "quux": ["bar", "banana"]
}

almost_solved = []

def recursive_find(key, so_far):
    global almost_solved
    for sub_key in dataset[key]:
        try:
            if sub_key in so_far:
                so_far.append(sub_key)
                almost_solved.append(so_far)
                return
            so_far.append(sub_key)
            return recursive_find(sub_key, so_far)
        except KeyError as e:
            so_far.pop(-1)
            continue


for key in dataset.keys():
    recursive_find(key, [])

intermediate_solution = []
for solution in almost_solved:
    intermediate_solution.append(set(solution))

solutions = []

while len(intermediate_solution) > 0:
    st = intermediate_solution.pop()
    if sorted(list(st)) not in [sorted(solution) for solution in solutions]:
        solutions.append(list(st))

final = []
for solution in solutions:
    print(*solution, solution[0])
