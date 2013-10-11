#!/usr/bin/env python3

## Lists ##

# create a list
a = [17, 15, 43, 73]

# read from a list
print(a[2]) # => 43

# update a list
a[0] = 42

# push to a list
a.append(17)

# pop from a list
x = a.pop()

# iterate over each list element
for x in a:
  print("-", x)

# iterate over each list index
for i in range(0, len(a)):
  print(i, "-", a[i])

# lists can contain mixed types!
a = [13, 'fun', 8.9, 'apple']

# create an empty list
a = [ ]
# and then push things to the list
a.append(7)
a.append(3)
a.append(4)
print(a) # => [7, 3, 4]

# lits can also contain other lists!
points = [[6, 3], [1, 2], [4, 5]]
print(points[1])    # => [1, 2]
print(points[0][1]) # => 3

# update works just the same
points[2] = [7, 5]
points[2][0] = 4

# quickly create empty arrays and matrices
a = [0] * 5
print(a) # => [0, 0, 0, 0, 0]

m = [[0] * 3] * 4
print(m)
# => [[0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]]

## Dictionaries

# a simple dictionary
tel = {'jack': 4098, 'sape': 4139}

# add a key-value pair to the dictionary
tel['guido'] = 4127

# note: the order of keys is arbitrary
print(tel) # => {'jack': 4098, 'guido': 4127, 'sape': 4139}

# modify the value of a key in a dictionary
tel['jack'] = 1234
print(tel) # => {'jack': 1234, 'guido': 4127, 'sape': 4139}

# remove a key from a dictionary
del tel['sape']
print(tel) # => {'jack': 1234, 'guido': 4127}

# test if a key is in the dictionary
if 'jack' in tel:
  print("jack is in the phone book")
else:
  print("jack is not in the phone book")

# note: you get an error if you try to delete a non-existent key
# so, if you don't know if the key is present, you might need to check first
if 'wiki' in tel:
  del tel['wiki']

# create an empty dictionary
d = { }
# and then add stuff to it, types can be mixed
d['a'] = 123
d['b'] = 'apple'
d[17] = 24
d[7.9] = 'thing'
# again note keys are in arbitrary order
print(d) # => {'a': 123, 17: 24, 'b': 'apple', 7.9: 'thing'}

# iterate over dictionary keys
for k in tel:
  print(k, "->")

# iterate over key-value dictionary pairs
for k, v in tel.items():
  print(k, "->", v)

# iterate over dictionary values
for v in tel.values():
  print("->", v)
  
# list and dictionaries can be mixed freely, for example to describe a graph
# using adjacency lists
graph = { 'a': ['b', 'c'], 'b': ['w'], 'w': ['c', 'a'] }

# or an adjacency graph with costs
graph = { 'a': {'b': 5, 'c': 7}, 'b': {'w': 1}, 'w': {'c': 7, 'a': 3} }
print("the cost from {0} to {1} is {2}".format('b', 'w', graph['b']['w']))

# often a list of "names" and a "cost" matrix are much easier!
name = ['a', 'b', 'c']
cost = [[None,    2,    3],
        [   2, None,    1],
        [   3,    1, None]]
print("the cost from {0} to {1} is {2}".format(name[0], name[2], cost[0][2]))

# Read a lot more at:
# http://docs.python.org/3/tutorial/datastructures.html
