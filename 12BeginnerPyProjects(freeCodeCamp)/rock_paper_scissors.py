import random

def rps():
    choices = ['r', 'p', 's']

    while True:
        choice = random.choice(choices)
        my_choice = input(f"what is your choice {choices} : ")
        print("i chose ", choice)
        if my_choice==choice:
            print("tied! \nlet's do it again...")
        elif choices.index(my_choice) == (choices.index(choice)+1)%3:
            print("you won!")
            break
        else:
            print("i won!")
            break

for i in range(10):
    rps()
        


    
