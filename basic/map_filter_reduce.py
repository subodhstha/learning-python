numbers = [1, 2, 3, 4, 5]
# result = map(lambda a: a*2, numbers)
# print(list(result))

# def isEven(n):
#     return n% 2 == 0

# result = filter(isEven, numbers)


# result = filter(lambda n : n %2 == 0, numbers)
# print(list(result))

from functools import reduce
expenses = [
    ('dinner',80),
    ('car repair',120)
]

sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)