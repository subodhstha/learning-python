INCH_IN_FEET = 12
def main():
    feet=float(input("Enter the length in feet "))
    inch = feet * INCH_IN_FEET
    print("The length is" ,inch,"inch")
if __name__ == '__main__':
    main()