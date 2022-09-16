"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

import random


def main():
    """
    TODO:
    """
    total = 0
    total2 = 0
    x = 1
    y = 1
    n = input('Which class? ')
    n = n.upper()
    a = random.randrange(1, 11)
    c = random.randrange(1, 11)
    maximum = a
    minimum = a
    total += a
    maximum2 = c
    minimum2 = c
    total2 += c
    if n == str(-1):
        print('No class score were entered')
    else:
        if n == 'SC001':
            print('Score ' + str(a))
        else:
            print('Score ' + str(c))
        while True:
            n = input('Which class? ')
            n = n.upper()
            if n == str(-1):
                break
            elif n == 'SC101':
                c = random.randrange(1, 11)
                print('Score ' + str(c))
                data2 = c
                y += 1
                total2 += c
                if data2 > maximum2:
                    maximum2 = data2
                if data2 < minimum2:
                    minimum2 = data2
                if n == str(-1):
                    break
            elif n == 'SC001':
                a = random.randrange(1, 11)
                print('Score ' + str(a))
                data = a
                x += 1
                total += x
                if data > maximum:
                    maximum = data
                if data < minimum:
                    minimum = data
                if n == str(-1):
                    break
        e = total / x
        d = total2 / y
        if y == 1:
            print('===========SC101============')
            print('No score for SC101')
        else:
            print('===========SC101============')
            print('Max(101) ' + str(maximum2))
            print('Min(101) ' + str(minimum2))
            print('Avg(101) ' + str(d))
        if x == 1:
            print('===========SC001============')
            print('No score for SC001')
        else:
            print('===========SC001============')
            print('Max(001) ' + str(maximum))
            print('Min(001) ' + str(minimum))
            print('Avg(001) ' + str(e))















# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
