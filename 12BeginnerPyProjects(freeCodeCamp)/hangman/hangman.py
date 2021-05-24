import words
import random

def hangman(lives):
    word = random.choice(words.valid_words)
    print(word)
    letters = set(word)
    used_letters = set()
    word_list = [letter if letter in used_letters else "_ " for letter in word]

    while lives>0:
        print()
        print(' '.join(word_list))
        print("you have used [", ' '.join(used_letters), "]. Remaining lives:", lives)
        guess = input("What is your next letter... : ")
        
        if guess in used_letters:
            print("you already used that, duh!")
            continue
        
        if ord(guess)<97 or ord(guess)>122:
            print("you have to use a lowercase alphabet!")
            continue
            
        used_letters.add(guess)
        
        if guess in letters:
            print("correct guess...!")
            letters.remove(guess)
            word_list = [letter if letter in used_letters else "_ " for letter in word]
        
        else:
            print("wrong guess...")
            lives -= 1
        
        if len(letters) == 0:
            print("you won! \nCorrect word is", word)
            break

        if lives == 0:
            print("you died!!")
            print("correct word was", word)
            break

hangman(10)
