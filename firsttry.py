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

dataset ={
        "foo": ["bar", "baz"],
        "orange": ["bnanana", "mango"],
        "bar": ["qux", "quux"],
        "monkey": ["cow", "parrot"],
        "banana": ["mango"],
        "baz": [],
        "quux": ["bar", "banana"]
}