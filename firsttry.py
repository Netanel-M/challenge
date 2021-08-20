import networkx

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


graph = networkx.DiGraph(dataset)

for cycle in networkx.simple_cycles(graph):
    x = cycle.copy()
    x.append(x[0])
    print(x)