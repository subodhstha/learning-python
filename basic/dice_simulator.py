import random
NUM_SIDES = 6
def main():
    dice1 = 10
    print("Dice in main() start as ",dice1)
    roll_dice()
    roll_dice()
    roll_dice
    print("dice1 in main is ",dice1)

def roll_dice():
    dice1 = random.randint(1,NUM_SIDES)
    dice2 = random.randint(1,NUM_SIDES)
    total = dice1 + dice2
    print("The total of two dice is ",total)
if __name__ == '__main__':
    main()