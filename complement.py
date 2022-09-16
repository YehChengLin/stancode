"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO:
    """
    build_complement()


def build_complement():
    ans = input("Please give me a DNA strand and I'll find the complement:  ")
    s = ''
    for i in range(len(ans)):
        alphabet = ans[i]
        if alphabet == 'A':
            s += 'T'
        elif alphabet == 'a':
            s += 'T'
        elif alphabet == 'A':
            s += 't'
        elif alphabet == 'a':
            s += 't'
        elif alphabet == 'T':
            s += 'A'
        elif alphabet == 't':
            s += 'A'
        elif alphabet == 'T':
            s += 'a'
        elif alphabet == 't':
            s += 'a'
        elif alphabet == 'G':
            s += 'C'
        elif alphabet == 'g':
            s += 'C'
        elif alphabet == 'G':
            s += 'c'
        elif alphabet == 'g':
            s += 'c'
        elif alphabet == 'C':
            s += 'G'
        elif alphabet == 'c':
            s += 'G'
        elif alphabet == 'C':
            s += 'g'
        elif alphabet == 'c':
            s += 'g'
    print('The complement of'+' '+ans+ " "+'is'+" "+s)



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
