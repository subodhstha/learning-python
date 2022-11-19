# tuple = ("max", 28, "Boston")
# tuple = "max", 28, "Boston"

# tuple = "max",
# print(type(tuple))

# tuple = ("max", 28, "Boston")
# print(tuple)

# item = tuple[1]
# print(item)

# for i in tuple:
#     print(i)

# if "yes" in tuple:
#     print("yes")
# else:
#     print("no")

# tuple2 = ("a", "b", "c", "d")
# print(len(tuple2))
# print(tuple2.count("o"))
# print(tuple2.count("a"))

# print(tuple2.index("a"))
# list = list(tuple2)
# print(list)

# tuple3 = tuple(list)
# print(tuple3)

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# b = a[2:]
# b = a[::2]
# b = a[::-1]

# print(b)


# tuple4 = "max", 28, "boston"

# name, age, city = tuple4
# print(name)
# print(age)
# print(city)

# tuple5 = (0, 1, 2, 3, 4, 5)

# i1, *i2, i3 = tuple5
# print(i1)
# print(i3)
# print(i2)

# list occupied more space than tuple
# import sys
# list = [0, 1, 2, "hello", True]
# tuple6 = (0, 1, 2, "hello", True)
# print(sys.getsizeof(list), "bytes")
# print(sys.getsizeof(tuple6), "bytes")

# tuple is faster than list
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]",number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)",number=1000000))