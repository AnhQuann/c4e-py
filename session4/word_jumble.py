from random import choice
words = ["champion", "football", "hello"]
word = choice(words)
word_list = list(word)
shuffle_word = []

for i in range(len(word)):
    charater = choice(word_list)
    shuffle_word.append(charater)
    word_list.remove(charater)

loop = True
while loop:
    print(*shuffle_word, sep=" ")
    input_answer = input("Your answer: ")
    if input_answer == word:
        print("Hura!")
        loop = False
    else:
        print("Wrong!")