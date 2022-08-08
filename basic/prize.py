def main():
    print("Welcome to game show")
    print("Pick the door 1,2 & 3 and win the prize")
    print("------------------------------------")
    door = int(input("Door: "))
    while door < 1 or door > 3 :
        print("Invalid Door ")
        door = int(input("Door: "))
    prize = 4
    if door == 1:
        prize = 2
    elif door ==2:
        locked = prize % 2 != 0 
        if not locked:
            prize += 6
    elif door == 3:
        for i in range(door):
            prize += i
    print("You win " + str(prize) + "treats")    
if __name__ == '__main__':
    main()