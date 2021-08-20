dataset ={
        "foo": ["bar", "baz"],
        "orange": ["bnanana", "mango"],
        "bar": ["qux", "quux"],
        "monkey": ["cow", "parrot"],
        "banana": ["mango"],
        "mango": ["banana"],
        "baz": [],
        "quux": ["bar", "banana"]
}
almost_solved = []

def recursive_find(key):
    global almost_solved
    for sub_key in dataset[key]:
        try:
            if (key == sub_key) or (key in dataset[sub_key]) or (sub_key in dataset[sub_key]):
                for index, name in enumerate(dataset[sub_key]):
                    if name == key or name == sub_key:
                        cycle_index = index
                almost_solved.append([key, sub_key, dataset[sub_key][cycle_index]])
            return recursive_find(dataset[sub_key])
        except:
            continue
for key in dataset.keys():
    recursive_find(key)

intermediate_solution = []
for solution in almost_solved:
    intermediate_solution.append(set(solution))

solutions = []

while len(intermediate_solution)> 0:
    st = intermediate_solution.pop()
    if list(st) not in solutions:
        solutions.append(list(st))

final = []
for solution in solutions:
    print(*solution, solution[0])
