# Sets: Unordered, mutable, no duplicates

set1 = {1,2,3,4,5,6,7}
set2 = {7,8,9,10,11,12,13}
setA = {1,2,3,4,5,6}
setB = {1,2,3}

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.remove(2)
myset.discard(4) # diff between remove() and discard() method is discard() will not throw any error if it not find any match element of the set
print(myset)
union = set1.union(set2)
print(union)

intersec = set1.intersection(set2)
print(intersec)

diff = set1.difference(set2)
print(diff)

symetric_diff = set1.symmetric_difference(set2)
print(symetric_diff)

set1.update(set2)
print(set1)

set1.intersection_update(set2)
print(set1)

set1.difference_update(set2)
print(set1)

set1.symmetric_difference_update(set2)
print(set1)

# Subset: setA all elements present in setB
print(setB.issubset(setA))

# Supreset: If 1st set contains all the elements of 2nd set
print(setA.issuperset(setB))

# Disjoint: If both set's elements are completly different from each other
print(setA.isdisjoint(set2))

# Copy two sets
setA = setB.copy()
setA =  set(setB)

# In forzenset it is immutable, you can't add or remove element from it once assigned
a = frozenset([1,2,3,4])

a.add(5)
a.remove(4)
print(a)