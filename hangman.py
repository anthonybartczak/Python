import random as r

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

    guess_list = [guessed_char if x == char_index else x for x in guess_list]

    #for index in char_index:
        #print(index)
        #guess_list[index] = guessed_char

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
char = input('Podaj literę: ')

if char in word:
    char_index = get_char_pos(word, char)
    updated_char = exchange_char(char_index, guess_list, char)
    print(updated_char)
else:
    print('Zła litera!')