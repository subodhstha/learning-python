SENTINEL = -1
def main():
    num = int(input("Enter the number "))
    total = 0
    while num != SENTINEL:
        total = total + num
        num = int(input("Enter the number "))
    print("Total is " + str(total))
if __name__ == '__main__':
    main()