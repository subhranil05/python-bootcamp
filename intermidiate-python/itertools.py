# Itertools: product, permutations, combinations, accumulate, groupby and infinite iterators

from itertools import product

a = [1,2]
b = [3,4]

prod = product(a,b)

print(list(prod))



from itertools import permutations

a = [1,2,3]

perm = permutations(a, 2)

print(list(perm))



from itertools import combinations, combinations_with_replacement

a = [1,2,3,4]

comb = combinations(a, 2)

comb_replace = combinations_with_replacement(a, 2)

print(list(comb))
print(list(comb_replace))



from itertools import accumulate
import operator

a = [1,2,3,4]

acc = accumulate(a)
acc_mul = accumulate(a, func= operator.mul)

print(list(acc))
print(list(acc_mul))



from itertools import groupby

def smaller_than_three(x):
    return x < 3

a = [1,2,3,4]

grpby = groupby(a, key=smaller_than_three)

for key, value in grpby:
    print(key, list(value))