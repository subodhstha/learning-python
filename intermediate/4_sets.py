# set doesn't allowed duplicates
# set1 = {1, 2, 3, 1, 2, }
# set1 = ([1, 2, 3])
# print(set1)
# set2 = set("hello")
# print(set2)

# set3 = {}
# set3 = set()
# set3.add(1)
# set3.add(2)
# set3.add(3)
# set3.add(4)
# print(set3)
# set3.remove(3)
# set3.discard(4)
# set3.pop()
# print(set3)
# set3.clear()
# print(set3)

# for i in set3:
#     print(i)
# if 3 in set3:
#     print("yes")

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}
# u = odds.union(evens)
# print(u)

# i = odds.intersection(primes)
# print(i)


# setA = {1, 2, 3, 4, 5, 6, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# dif = setA.difference(setB)
# dif = setB.symmetric_difference(setA)
# print(dif)

# setA.update(setB)
# setA.intersection_update(setB)
# setA.difference_update(setB)
# print(setA)

from calendar import setfirstweekday


setC = {1, 2, 3, 4, 5, 6}
# setD = {1, 2, 3}
# setE = {7, 8}
# print(setD.issuperset(setC))
# print(setC.issuperset(setD))
# print(setD.isdisjoint(setC))
# print(setD.isdisjoint(setE))


setF = set(setC)
setF.add(9)
print(setF)
print(setC)


a = frozenset([1, 2, 3, 4])
a.add(2)
print(a)