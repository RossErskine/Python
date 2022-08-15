# -*- coding: utf-8 -*-
"""
Script looking at basic python
Data structure and sequences

"""
 # Tuples
tup = 4, 5 ,6
tup

# Nested tuples
nested_tup = (4, 5, 6), (7, 8, 9)
nested_tup

# String tuples
stup = tuple('string')
stup

stup[0] 

# Mixed tuples
mtup = tuple(['foo', [1, 2], True])
mtup[1].append(3)
mtup

# Concatenate tuples
contup = (4, None, 'foo') + (6, 0)+ ('bar',)
contup

# Multply tuples
multup = ('foo', 'bar')*4
multup

# Unpacking tuples
a, b, c = tup
b

seqtup = 4, 5, (6, 7)
a, b, (c, d) = seqtup
seqtup

# Swapping 
a, b = 1, 2
a
b

b, a = a, b
a
b 

# unpacking a sequence
seq = [(1, 2, 3), (4, 5, 6),(7, 8, 9)]
for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))
    
# plucking elements
values = 1, 2, 3, 4, 5
a, b, *rest = values
a, b

rest

# tuple methods
a = (1, 2, 2, 2, 3, 4, 2)
a.count(2)

# Lists
a_list = [2, 3, 7, None]
a_tup =('foo', 'bar', 'baz')
b_list = list(a_tup)
b_list

# Change item in list
b_list[1] = 'peekaboo'
b_list

# generate list
gen = range(10)
gen
list(gen)

# append list
b_list.append('dwarf')
b_list

# insert index i list
b_list.insert(1, 'red')
b_list

# pop off index i list
b_list.pop(2)
b_list

# remove first item of type from list
b_list.append('foo')
b_list
b_list.remove('foo')
b_list

# check list of value using keywords
'dwarf' in b_list
'dwarf' not in b_list

# Concatenate list
[4, None, 'foo']+[7, 8,(2, 3)]
x = [4, None, 'foo']
x.extend([7, 8, (2, 3)])
x

# Sorting lists
a = [7, 2, 5, 1, 3]
a.sort()
a

b = ['saw',' small', 'he', 'foxes', 'six']
b.sort(key=len)
b

# binary search
import bisect
c = [1, 2, 2, 2, 3, 4, 7]
bisect.bisect(c, 2)
bisect.bisect(c, 5)
bisect.insort(c, 6)
c

# slicing [start:stop]
seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[1:5]

# assign sequence
seq[3:4] = [6, 3]
seq

# omit stop
seq[3:]
# omit start
seq[:5]
# negative slicing from end
seq[-4:]

# [start:stop:step] slicing
seq[::2]

# reverse slicing
seq[::-1]

# enumerate
some_list = ['foo', 'bar', 'baz']
mapping = {}

for i, v in enumerate(some_list):
    mapping[v] = i

mapping

# Zip pairs
seq1 = ['foo','bar','baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
list(zipped)

# Zip shortest seq
seq3 = [True, False]
list(zip(seq1, seq2, seq3))

# combine zip and enumerate
for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))
    
# unzip using zip
pitchers = [('Nolan', 'ryan'), ('roger', ' clemens'), ('schilling', 'curt')]
first_names, last_names = zip(*pitchers)
first_names
last_names

# dictionaries
empty_dict = {}
d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
d1

d1[7] = 'an integer'
d1

d1['b']

# del dict
del d1[7]
d1

# dict keys
list(d1.keys())
# dict values
list(d1.values())

# merg dict
d1.update({'b': 'foo', 'c':12})
d1

# valid dict types
hash('string')

# Sets (unique elements)
set([2, 2, 2, 1, 3, 3])

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

# Union
a.union(b)
# or
a | b
# Intersect
a.intersection(b)
# or
a & b

# Comprehensions
# [expr for val in collection if condition]
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]

unique_lengths = {len(x) for x in strings}
unique_lengths

local_mapping = {val : index for index, val in enumerate(strings)}
local_mapping

# Functions
states = ['   Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlOrida', 
          'south    carolina##', 'West virginia?']

import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]','', value)
        value = value.title()
        result.append(value)
    return result

clean_strings(states)

# lambda
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)

# Generators
some_dict = {'a':1, 'b': 2, 'c': 3}
dict_iterator = iter(some_dict)
list(dict_iterator)

# Itertools
import itertools
first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # names is a generator
    
# Errors and exception handling
def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x
    
attempt_float('something')