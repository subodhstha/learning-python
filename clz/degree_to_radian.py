#Write a Python code that takes the degree as input from the user and convert it into radian.
import numpy
def main():
    print("Enter the degree")
    a = int(input())
    y = numpy.deg2rad(a) 
    print("The angle in radian is ",y)
if __name__ == '__main__':
    main()