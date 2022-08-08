import random
NUM_SIDES = 6
def main():
    die1 = random.randint(1,NUM_SIDES)
    die2 = random.randint(1,NUM_SIDES)
    total = die1 + die2
    print("Dice have ",NUM_SIDES ,"side of each.")
    print("First die is",die1)
    print("Second die is",die2)
    print("Total of two dice is",total)
if __name__ == '__main__':
    main()