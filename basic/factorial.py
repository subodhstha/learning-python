MAX_NUM = 4
def main():
    for i in range(MAX_NUM):
        print(i,factorial(i))
        
def factorial(n):
    result = 1
    for i in range(1, n+1 ):
        result *= i
    return result
if __name__ == '__main__':
    main()
     