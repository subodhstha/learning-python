"""Write a Python code to calculate Permutation (5,3)"""
from itertools import permutations
def main():
    perm = permutations([1,2,3,4,5],3)
    print("The permutations are")
    for i in list(perm):
        print(i)
if __name__ == '__main__':
    main()