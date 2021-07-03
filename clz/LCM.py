#Write a Python code to calculate LCM of (25,55)
def main():
    a = 25
    b = 55
    if(a > b):
        max = a
    else:
        max = b
    while (True):
        if(max % a == 0 & max % b == 0):
            print("lcm is ",max)
            break;
        max = max + 1
if __name__ == '__main__':
    main()