import random
from statistics import mean
# a = random.random()
# a = random.uniform(1,10)
# a = random.randint(1, 10)
# a = random.randrange(1, 10)

# normalvariate(mean,standard deviation)
# a = random.normalvariate(0, 1)

list1 = list("ABCDE")
# a = random.choice(list1)
# a = random.sample(list1, 3)
# a = random.choices(list1, k=3)
# print(a)
# random.shuffle(list1)
# print(list1)
# random.seed(1)
# print(random.random())
# print(random.randint(1,10))

# random.seed(2)
# print(random.random())
# print(random.randint(1,10))

# random.seed(1)
# print(random.random())
# print(random.randint(1,10))

# random.seed(2)
# print(random.random())
# print(random.randint(1,10))

import secrets

# a = secrets.randbelow(10)
# print(a)

# b = secrets.randbits(4)
# print(b)

# list2 = list("ABCD")
# c = secrets.choice(list2)
# print(c)

import numpy as np
# a = np.random.rand(3)
# a = np.random.randint(0,10)
# a = np.random.randint(0,10,3)
# a = np.random.randint(0,10, (3,4))

# print(a)

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# np.random.shuffle(arr)
# print(arr)

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))