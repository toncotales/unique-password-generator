"""
    unique password generator

    Generate a unique password string from 12 to 32 characters in length

    :author: Anthony Cotales
    :email: acotales@protonmail.com
"""
# A tribute to my deceased mother on her 40 days (T.T) 08-27-2022
__author__ = 'Anthony Cotales'

import argparse
import string
import random


def random_sample() -> str:
    """Returns a string with a variety of characters"""
    digits = random.sample(string.digits, 2)
    punctuation = random.sample(string.punctuation, 2)
    uppercase = random.sample(string.ascii_uppercase, 2)
    lowercase = random.sample(string.ascii_lowercase, 2)
    random_characters = set(digits + punctuation + uppercase + lowercase)
    return str().join(random_characters)


def password_logic(sample: str) -> str:
    """Password complexity logic function"""
    def char_type(c: str) -> str:
        if c.isupper():
            return "upper"
        elif c.islower():
            return "lower"
        elif c.isnumeric():
            return "digit"
        elif c.isspace():
            return "space"
        else:
            return "punctuation"

    # Using a while loop to arrange the characters in a nonconsecutive order
    while True:
        # Boolean list to determine if the string is in nonconsecutive order
        nonconsecutive = [
            char_type(sample[i]) != char_type(sample[i + 1])
            for i in range(len(sample) - 1)
        ]
        # Break out of the loop when conditions are satisfied
        if all(nonconsecutive):
            break
        # If conditions are not met rearrange the order of characters
        sample = str().join(random.sample(sample, len(sample)))
    return sample


def generate_password(length=14) -> str:
    """Returns a unique string that can be used as password"""
    # Info: Be aware in adding or removing characters in the
    # variable of excluded_characters as it will relatively alter
    # the length requirement and/or the process of the output string
    excluded_characters = "\"(),./:;<>'[\\]`{}~"
    length = 12 if length < 12 else 32 if length > 32 else length
    password = str()
    for _ in range(32):
        sample = random_sample()
        for n in sample:
            if n not in excluded_characters and n not in password:
                password += n
    return password_logic(password[:length])


if __name__ == "__main__":
    USAGE = """\n\
$ python upgen.py\n\
$ python upgen.py -l 12\n\
$ python upgen.py --length 32\
 """
    parser = argparse.ArgumentParser(description="info: generate a password from 12 to 32 characters in length")
    parser.usage = USAGE
    parser.add_argument("-l", "--length", type=int, required=False, metavar="",
                        default=14, help="length of the unique string")
    args = parser.parse_args()
    print(generate_password(args.length))
