"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:
    """
    create_new_alphabet()


def create_new_alphabet():
    key = int(input('Secret Number: '))
    new_alphabet = ''
    first_half = ALPHABET[0:key]
    second_half = ALPHABET[key:]
    new_alphabet = second_half + first_half
    n = input("What's the ciphered string ? ")
    n = n.upper()
    ans = ''
    for i in range(len(n)):
        ch = n[i]
        if not ch.isalpha():
            ans += ch
        for j in range(len(ALPHABET)):
            if ch == ALPHABET[j]:
                ans += new_alphabet[j]
                break
    print('The deciphered string is :'+' '+ans)
















# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
