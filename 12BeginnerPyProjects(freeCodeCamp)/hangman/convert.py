with open('words.txt') as wordfile:
    words = list(set(wordfile.read().split()))

print(words)

f = open('words.txt', 'w')
f.write(f'valid_words = {words}')
f.close()
