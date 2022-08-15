def main():
    print("Think the value from 0 t0 100")
    max_value = 100
    min_value = 0
    while True:
        query = min_value + (max_value -min_value) // 2
        if check_answer(query) :
            break
        if check_greater(query):
            min_value = query + 1
        else:
            max_value = query -1
    print("your number was ",query)

def check_answer(value):
    return ask_true_false("Is your answer " +str(value)+"?")

def check_greater(value):
    return ask_true_false("Is your number is greater than "+str(value)+"?")

def ask_true_false(prompt):
    respose = input(prompt+ "y/n")
    return respose == "y" or respose == "Y"

if __name__ == '__main__':
    main()