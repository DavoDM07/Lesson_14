#○ Write a function that generates a random password for the user. Allow the user to
#specify the length and complexity of the password (include letters, numbers, andsymbols).
#Ogtvel random u string module-neric (string.ascii_letters,string.digits,string.punctuation, )
from string import ascii_letters, digits, punctuation
from random import shuffle, choice

def random_password_generator(length, letter, digit, symbol):
    symbols = ''
    if letter:
        symbols += ascii_letters
    if digit:
        symbols += digits
    if symbol:
        symbols += punctuation
    password = []
    if letter:
        password.append(choice(ascii_letters))
    if digit:
        password.append(choice(digits))
    if symbol:
        password.append(choice(punctuation))
    while len(password) < length:
        password.append(choice(symbols))
    shuffle(password)
    return ''.join(password)

print(random_password_generator(7,True,True,False))




