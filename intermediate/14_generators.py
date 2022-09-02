# def myGenerator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# g = myGenerator()
# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)

# print(sum(g))
# print(sorted(g))



# def Countdown(num):
#     print("string")
#     while num > 0:
#         yield num
#         num -= 1
        
# cd = Countdown(4)

# value = next(cd)
# print(value)

# print(next(cd))
# print(next(cd))
# print(next(cd))




# import sys

# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# print(firstn(10))
# print(sum(firstn(10)))


# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
        
# print(sys.getsizeof(firstn(1000)))
# print(sys.getsizeof(firstn_generator(1000))) // use less memory space



# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b

# fib = fibonacci(30)
# for i in fib:
#     print(i)


import sys
myGenerator = (i for i in range(10) if i % 2 == 0)
# for i in myGenerator:
#     print(i)
# print(list(myGenerator))
print(sys.getsizeof(myGenerator))

myList = [i for i in range(10) if i % 2 == 0]
# print(myList)
print(sys.getsizeof(myList))