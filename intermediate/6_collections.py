# from collections import Counter
# a = "baaaaaaaaaadsdsferdsfdadsfadsfa"
# counter1 = Counter(a)
# # print(counter1)
# # print(counter1.values())
# # print(counter1.most_common())
# # print(counter1.most_common(1))
# # print(counter1.most_common(2)[0])
# # print(counter1.most_common(2)[0][0])
# print(list(counter1.elements()))

# from collections import namedtuple
# Point = namedtuple("Point", "x,y")
# pt = Point(1, -4)
# print(pt)
# print(pt.x, pt.y)\
    
    
# from collections import OrderedDict
# # ordered_dict = OrderedDict()
# ordered_dict = {}
# ordered_dict["a"] = 1
# ordered_dict["b"] = 3
# ordered_dict["c"] = 2
# ordered_dict["d"] = 5
# ordered_dict["e"] = 4
# print(ordered_dict)

# from collections import defaultdict
# d = defaultdict(int)
# d["a"] = 1
# d["b"] = 2
# d["c"] = 3
# # print(d["b"])
# print(d["d"])


from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.extend([4, 5, 6])
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)