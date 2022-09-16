"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dictionary = {}


def main():
    """
    TODO:
    """
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        start = time.time()
        result = find_anagrams(s, '', [])
        print(result)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    

def read_dictionary():
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            line2 = line.replace('\n', "")
            dictionary[line2] = len(line2)
            

def find_anagrams(s, prefix, result):
    if s == '':
        result.append(prefix)
        print('Searching....')
        print('Found:  ', prefix)
        return result
    for i in range(len(s)):
        if s[0] != s[i] or i == 0:
            s = swap(s, i)
            prefix = list(prefix)
            prefix.append(s[0])
            prefix = ''.join(prefix)
            if has_prefix(prefix, len(s)+len(prefix)-1):
                remain = ''
                for j in range(1, len(s)):
                    remain = list(remain)
                    remain.append(s[j])
                    remain = ''.join(remain)
                result = find_anagrams(remain, prefix, result)
            prefix = list(prefix)
            prefix.pop()
            prefix = ''.join(prefix)
            swap(s, i)
    return result


def has_prefix(sub_s, length):
    global dictionary
    for key in dictionary:
        if dictionary[key] == length and key.startswith(sub_s):
            return True
    return False


def swap(s, i):
    s = list(s)
    temp = s[0]
    s[0] = s[i]
    s[i] = temp
    s = ''.join(s)
    return s

if __name__ == '__main__':
    main()
