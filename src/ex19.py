"""
Exercise 19 : Password Generator
"""
import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'    # 26 characters
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26 characters
NUMBERS = '1234567890'                          # 10 characters
SPECIAL = '~!@#$%^&*()_+'                       # 13 characters

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL

def gen_password(l):
    """
    Generates a password of at least 12 characters including at least one lowercase, one uppercase,
    one digit, and one special character.

    Parameters:
        l (int): Desired length of the password.

    Returns:
        str: The generated password.
    """
    # FIX : complete this
    if l < 12:
        l = 12

    pw = []

    pw.append(LOWER_LETTERS[random.randint(0, 25)])
    pw.append(UPPER_LETTERS[random.randint(0, 25)])
    pw.append(NUMBERS[random.randint(0, 9)])
    pw.append(SPECIAL[random.randint(0, 12)])
    while len(pw) < l:
        pw.append(ALL_CHARS[random.randint(0, 74)])
    random.shuffle(pw)
    return ''.join(pw)
