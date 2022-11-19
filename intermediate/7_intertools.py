# product, permutations, combinations, accumulate, groupby, infinite iterators
# from itertools import product
# # a = [1, 2]
# # b = [3, 4]
# a = [1, 2]
# b = [3]
# prod = product(a, b, repeat=2)
# print(list(prod))

# from itertools import permutations
# # a = [1, 2, 3]
# # perm = permutations(a)
# # print(list(perm))
# a = [1, 2, 3]
# perm = permutations(a, 2)
# print(list(perm))

# from itertools import combinations
# a = [1, 2, 3, 4]
# comb = combinations(a,3)
# print(list(comb))


# from itertools import combinations_with_replacement
# a = [1, 2, 3, 4]
# comb = combinations_with_replacement(a,3)
# print(list(comb))

# from itertools import accumulate
# import operator  
# # a = [1, 2, 3, 4]
# # acc = accumulate(a)
# # print(a)
# # print(list(acc))
# # a = [1, 2, 3, 4]
# # acc = accumulate(a, func= operator.mul)
# a = [1, 2, 9, 3, 4]
# acc = accumulate(a, func= max)
# print(a)
# print(list(acc))



from itertools import groupby
# def smaller_than_3(x):
#     return x < 3

# a = [1, 2, 3, 4]
# group_obj = groupby(a, key=smaller_than_3)
# # print(group_obj)
# for key, value in group_obj:
#     print(key, list(value))



# a = [1, 2, 3, 4]
# group_obj = groupby(a, key= lambda x: x<3)
# # print(group_obj)
# for key, value in group_obj:
#     print(key, list(value))
  
  
# persons = [{"name" : "Tim", "age": 26}, {"name": "Dan", "age": 26},
#            {"name" : "Harry", "age": 28}, {"name": "Tom", "age": 27},
#            {"name" : "Jerry", "age": 27}, {"name": "Bob", "age": 26}]

# group_obj = groupby(persons, key = lambda x: x["age"])
# for key, value in group_obj:
#     print(key, list(value))


from itertools import count, cycle, repeat
# for i in count(10):
#     print(i)
#     if i == 15:
#         break

# a = [1, 2, 3]
# for i in cycle(a):
#     print(i)

for i in repeat(1, 7):
    print(i)