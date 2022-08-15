import random
def main():
    secret_num = random.randint(1,99)
    print("I am thinking the number 1 to 99 guess the number.")
    guess = int(input("Guess the humber "))
    while guess != secret_num:
        if guess > secret_num:
            print("The number you guess is high.")
        else:
            print("The number you guess is low.")
        print("")
        guess = int(input("Enter the new guess "))
    print("Congratulation you guess the correct number " + str(guess)  )
if __name__ == '__main__':
    main()