import string
import random

def generate_one_time_psswd(length):
    characters = string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password