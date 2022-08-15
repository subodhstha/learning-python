def main():
    print("Welcome to game show")
    print("Pick the door 1,2 & 3 and win the prize")
    print("------------------------------------")
    door = get_door_choose()
    prize = calculate_prize(door)
    print("You win " + str(prize) + "treats")

def get_door_choose():
    door = int(input("Door: "))
    while door < 1 or door > 3 :
        print("Invalid Door ")
        door = int(input("Door: "))
        return door

def calculate_prize(door):
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
    return prize

if __name__ == '__main__':
    main()