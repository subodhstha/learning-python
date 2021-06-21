def main():
    x = 3
    x = add_five(x)
    print("x = ",x )

def add_five(x):
    x = x + 5
    return x

if __name__ == '__main__':
    main()