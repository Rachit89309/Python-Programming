#  use curly braces {}
# duplicates items are not allowed
# they have not defined order
# indexing is not allowed b/c these are unordered
# set items are unchangeable

set1 = {10, 56, 89, 98, 'jenny', True}
print(set1)
set2 = {}
set3 = set()

print(type(set1))
print(type(set2))
print(type(set3))

# slicing is not allowed
# set object does not support item assignment
print(len(set1))
set1.remove(10)
print(set1)

# except remove if we use discard it print orignal set
set1.discard(68)
print(set1)


#  some operations on set
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Rachit'}

# union
print(set1.union(set2))
print(set1 | set2)
#  we can do the union of multiple sets
print(set1.union(set2, set3))

print(set1.union(('Mohan', 'Jenny')))
set1.update(set2)    # or set1 |= set2
print(set1)


# case sensitive is allowed
# intersection

a = {'ram', 'shyam', 'jenny'}
b = {'jenny', 'jiya', 'aakash'}
print(a.intersection(b))
print(a & b)
a.intersection_update(b)
print(a)

# symmetric difference and symmetric difference update
c = {'a', 'b', 'ra'}
d = {'ra', 'd', 'e'}
e = {'f', 'g'}
#  difference gives the items which are present in c but not in d
c.difference(d)   # or print(c - d)
print(c)

print(c.difference(d, e))
c.difference_update(d)
print(c)

# symmetric difference -> The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
print(c.symmetric_difference(d))
print(c ^ d)

d.symmetric_difference_update(c)
print(d)


# disjoint set -> if they have nothing in common, there intersection is an empty set
print(c.isdisjoint(d))

f = {1, 2, 3, 4, 5}
g = {4, 10, 7, 8, -10, 1, 3, 2, 5}
# c is subset of d if every element of c is in d
print(f.issubset(g))

# superset is the reverse of subset -> it means that f contains all the elements of g if it satisfy the condition then true otherwise false
print(f.issuperset(g))

 



