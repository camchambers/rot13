# Define a translation table to perform the mapping between characters
rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                       'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

# A function to perform the translation
def rot13(text):
    """ Translate the text """
    return text.translate(rot13trans)


def main():
    txt = "The quick brown fox jumps over the lazy dog"
    print(rot13(txt))


if __name__ == "__main__":
    main()
