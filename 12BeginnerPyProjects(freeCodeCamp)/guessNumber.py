import random

def guess(n):
    random_num = random.randint(1, n)
    guess_num = 0

    while guess_num != random_num:
        guess_num = int(input(f"Guess a number between 1 and {n} : "))
        if guess_num < random_num:
            print("number less than true value...")
        elif guess_num > random_num:
            print("too high dude...")
    print("congrats!")


guess(10)

def comp_guess(n):

    low = 1
    high = n

    while True:
        guess_num = random.randint(low, high)
        print(f"i guessed ... {guess_num}")
        validate = input("is the number high(h), low(l) or correct(c) : ")
        if validate=='c':
            print("I won...!")
            break
        elif validate=='h':
            high = guess_num - 1
        elif validate == 'l':
            low = guess_num + 1
        else:
            print("please give a valid feedback next time!")

        print("okay, i'll guess again...")
        
comp_guess(30)