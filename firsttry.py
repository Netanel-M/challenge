'''
┌────
│ {
│   "foo": ["bar", "baz"],
│   "orange": ["bnanana", "mango"],
│   "bar": ["qux", "quux"],
│   "monkey": ["cow", "parrot"],
│   "banana": ["mango"],
│   "baz": [],
│   "quux": ["bar", "banana"],
│   ...
│ }
└────

Write a program that finds all the cycles in this file:

In the example above we can have the cycle: `"bar" -> "quux" -> "bar"'

Make sure that:

• Every cycle is represented only once, e.g. `"bar" -> "quux" -> "bar"'
  is the same cycle as `"quux" -> "bar" -> "quux"'.
• Only minimal cycles should be shown, e.g. in `"foo" -> "bar" -> "quux"
  -> "bar"' The `"foo" ->' should not be part of the cycle.

Please deliver your solution as a link to a Git repository or a tarball
of that repository.  Try to commit often.
'''

def find_path(master_key, subarray, original, so_far):
    #print("###################")
    #print(master_key)
    for i in subarray:
        try:
            if not i in so_far:
                so_far.append(i)
                find_path(i, dataset[i], original, so_far)
            else:
                print("$$$$$$$$$$")
                so_far.append(i)
                print(so_far)
                return
        except KeyError:
            so_far.remove(i)
            continue
dataset ={
        "foo": ["bar", "baz"],
        "orange": ["bnanana", "mango"],
        "bar": ["qux", "quux"],
        "monkey": ["cow", "parrot"],
        "banana": ["mango"],
        "baz": [],
        "quux": ["bar", "banana"]
}
solutions = []
for master_key in dataset.keys():
    try:
        subarray = dataset[master_key]
    except:
        raise
    find_path(master_key, subarray,master_key, [])
    #exit()
