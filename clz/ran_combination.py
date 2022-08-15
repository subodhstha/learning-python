#Ask enter to enter two numbers (say, a and b). Generate two random numbers between those two numbers and find a combination of these two newly generated random numbers.  
import random
import math
def main():
    print("Enter any two number ")
    a = int(input())
    b = int(input())
    c = math.comb(a,b)
    if (a>b):
        d = random.randint(b,a)
        print("Random of between the number is ",d)
    elif(b>a):
        d = random.randint(a,b)
        print("Random of between the number is ",d)
    print("Combination of number is ",c)
    
if __name__ == '__main__':
    main()