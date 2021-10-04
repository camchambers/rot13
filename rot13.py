#!/usr/bin/python3

import sys
# Define a translation table to perform a mapping between characters
rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                           'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')


def encrypt(text):
    """ Translate the text """
    return text.translate(rot13trans)


def main():
    for line in sys.stdin:
        sys.stdout.write(encrypt(line))


if __name__ == "__main__":
    main()
