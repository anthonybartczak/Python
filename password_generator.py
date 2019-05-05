import random as r
import string as s

def create_strong(length):

    iter = 0
    password = ''
    while iter < length:

        num_or_let = r.randrange(1, 3)

        if num_or_let == 1:
            add = r.choice(s.ascii_letters)
            password = password + add
            iter += 1

        elif num_or_let == 2:
            add = r.randrange(0,9)
            password = password + str(add)
            iter += 1

    return password

lol = create_strong(20)
print(lol)