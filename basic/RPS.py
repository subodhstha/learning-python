import random
NO_GAMES = 3

def main():
    print_welcome()
    score = 0
    for i in range(NO_GAMES):
        ai_move = get_ai_move()
        human_move = get_human_move()
        result  = out_come_result(ai_move,human_move)
        announce_result(ai_move,result)
        score += out_come_score(result)
    print('your score', score)

def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(NO_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissor beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')

def get_ai_move():
    value = random.randint(1, 3)
    if value == 1:
        return "rock"
    if value ==2:
        return "paper"
    else:
        return "scissor"

def get_human_move():
    while True:
        choice = input("what do you want to play ")
        if valid_choice(choice):
            return choice
        print("The input is invalid choice")

def valid_choice(choice):
    if choice == "rock":
        return True
    if choice == "paper":
        return True
    if choice == "scissor":
        return True
    else:
        return False

def out_come_result(ai_move,human_move):
    if ai_move == human_move:
        return "tie"
    if ai_move == "rock":
        if human_move == "scissor":
            return "ai"
        return "human"
    if ai_move == "scissor":
        if human_move == "paper":
            return "ai"
        return "human"
    if ai_move == "paper":
        if human_move == "rock":
            return "ai"
        return "human"

def out_come_score(result):
    if result == "human":
        return +1
    if result == "ai":
        return -1
    return 0
    
def announce_result(ai_move, result):
    print('The AI plays: ' + ai_move)
    print('The winner is: ' + result)
    print('')
    
if __name__ == '__main__':
    main()