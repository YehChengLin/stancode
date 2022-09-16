"""
File: similarity.py (extension)
Name:
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO:
    """
    DNA = input('Please give me a DNA to search: ')
    test = input('What DNA would you like to match? ')
    s = ''
    n = ''
    for i in range(len(DNA)-len(test)+1):
        ch = DNA[i]
        for j in range(len(test)):
            ch2 = test[j]
            if ch =
















# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
