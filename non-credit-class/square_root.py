#Write a Python code that inputs input from the user and calculate its square root.
import math
def main():
    a = int(input("Enter the number "))
    b = math.sqrt(a)
    print("Square root is",b)
if __name__ == '__main__':
    main()