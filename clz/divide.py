#Divide 1000 by 3 and print the answer with only 5 numbers after decimal.
def main():
    a = 100
    b = 3
    c = float("{:.5f}".format(a/b))
    print("When ",str(a) +" divide ",str(b) +" the result is",c)
if __name__ == '__main__':
    main()