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
from numpy import roll
almost_solved = []

def recursive_find(key):
    global almost_solved
    #print(ntry)
    #total_tries.append([key])
    for sub_key in dataset[key]:
        try:
            #total_tries[index].append(sub_key)
            if (key == sub_key) or (key in dataset[sub_key]) or (sub_key in dataset[sub_key]):
                almost_solved.append([key, sub_key, dataset[sub_key][0]])
                #print(key, sub_key, dataset[sub_key])
            return recursive_find(dataset[sub_key])
        except:
            continue
for key in dataset.keys():
    recursive_find(key)

print(almost_solved)