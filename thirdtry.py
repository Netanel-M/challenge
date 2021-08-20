
# Modified dataset for increased testing
dataset ={
        "foo": ["bar", "baz"],
        "orange": ["bnanana", "mango"],
        "bar": ["qux", "quux"],
        "monkey": ["cow", "parrot"],
        "banana": ["mango"],
        "mango": ["banana"],
        "baz": ["monkey"],
        "cow": ["baz"],
        "quux": ["bar", "banana"]
}

# where initially I will put possible matches
almost_solved = []

def recursive_find(key, so_far):
    # takes a key and a list of the current history of the path
    global almost_solved # simplify things a bit. Should've wrapped it in an object to avoid global variables maybe
    for sub_key in dataset[key]:
        try:
            if len(so_far) > 0 and so_far[0] == sub_key:
                # if the current key is equal to the first item in the history append it to history
                so_far.append(sub_key)
                # and add it to possible solutions
                almost_solved.append(so_far)
                #print(so_far)
                return
            # if it's not a cycle add the key to the history
            so_far.append(sub_key)
            # If you haven't hit the base case recurse on
            return recursive_find(sub_key, so_far)
        except KeyError as e:
            # Non existent index, rmeove it from path and continue to the next iteration
            so_far.pop(-1)
            continue


for key in dataset.keys():
    # this runs the above function on every key in the dataset
    recursive_find(key, [])

intermediate_solution = []
for solution in almost_solved:
    solution.pop() # lose the last item, it will screw everything up when we sort the lists
    intermediate_solution.append(solution)

solutions = []

while len(intermediate_solution) > 0:
    current_item = intermediate_solution.pop() # get an item we remove from the intermediate list
    if not (sorted(current_item) in [sorted(solution) for solution in intermediate_solution]): # check if the sorted item exists in the list where every item is sorted (check if duplicate exists)
        solutions.append(current_item) # add the unique item


final = []
for solution in solutions:
    print(*solution, solution[0]) # we add the last item back in
