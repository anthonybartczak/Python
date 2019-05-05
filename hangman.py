import random as r
import string as s

words_tpl = (
    #'car',
    'animal',
    #'vehicle',
    #'propane',
    #'basement',
)

word = list(r.choice(words_tpl))

#-----------------------------------------------------------------------------------------------------------------------

def show_blanks(word):

    guess_list = []

    for letter in word:
        letter = '_'
        guess_list.append(letter)

    return guess_list

#-----------------------------------------------------------------------------------------------------------------------

def exchange_char(char_index, guess_list, guessed_char):

    for index in char_index:
        guess_list[index] = guessed_char

    return guess_list

# -----------------------------------------------------------------------------------------------------------------------

def get_char_pos(word, guessed_char):

    char_index = []

    for count, char in enumerate(word):
        if char == guessed_char:
            char_index.append(count)

    return char_index

# -----------------------------------------------------------------------------------------------------------------------

guess_list = show_blanks(word)

print('Wyświetlam rozmiar słowa:', guess_list)

while '_' in guess_list:

    char = input('\nPodaj literę: ')

    if char in word:
        char_index = get_char_pos(word, char)
        updated_char = exchange_char(char_index, guess_list, char)
        for x in updated_char:
            print(x, end='')
    else:
        print('Zła litera!')