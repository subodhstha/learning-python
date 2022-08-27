# string1 = "Hello World"
# string1 = "Hello World\nI'm a student"
# string2 = """Hello world
# I am student"""
# print(string1)
# print(string2)

# char = string1[-2]
# substring = string1[1:4]
# substring = string1[::2]
# substring = string1[::-1]
# print(substring)

# greeting = "Hello"
# name = "Tom"
# sentence = greeting + " " + name
# print(sentence)
# for i in greeting:
#     print(i)
# if "e" in greeting:
#     print("yes")
# else:
#     print("no")

# string3 = "        hello world   "
# string3 = string3.strip()
# print(string3.upper())
# string4 = "hello world"
# print(string4.startswith("h"))
# print(string4.endswith("world"))
# print(string4.find("o"))
# print(string4.count("o"))
# print(string4.replace("world", "Nepal"))


# string5 = "how are you doing?"
# list1 = string5.split()
# string5 = "how,are,you,doing?"
# list1 = string5.split(",")
# new_string = " ".join(list1)
# print(new_string)

# from timeit import default_timer as timer

# list2 = ["a"] * 10000
# print(list2)

# # bad
# start = timer()
# string6 = ""
# for i in list2:
#     string6 += i
# stop = timer()
# print(stop-start)
# # print(string6)

# # good
# start = timer()
# string7 = "".join(list2)
# stop = timer()
# print(stop-start)
# # print(string7)


# var = "Tom"
# string8 = "the variable is %s" % var
var = 2.168464154
var2 = 49
# string8 = "the variable is %.3f" % var
# string8 = "the variable is {:.2f} and {}.".format(var,var2)
string8 = f"the variable is {var*2} and {var2}"
print(string8)