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

import time

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

def main():
    dictionary = read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        start = time.time()
        result = find_anagrams(s, dictionary)
        print(result)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')

def read_dictionary():
    dictionary = set()
    with open(FILE, 'r') as f:
        for line in f:
            dictionary.add(line.strip())
    return dictionary

def find_anagrams(s, dictionary):
    result = []
    find_anagrams_helper(s, '', result, dictionary)
    return result

def find_anagrams_helper(s, prefix, result, dictionary):
    if prefix in dictionary and prefix not in result:
        print('Searching....')
        print('Found: ', prefix)
        result.append(prefix)
    if not s:
        return
    for i in range(len(s)):
        if i > 0 and s[i] == s[i-1]:
            continue  # Skip duplicate characters to avoid redundant work
        find_anagrams_helper(s[:i] + s[i+1:], prefix + s[i], result, dictionary)

def has_prefix(sub_s, dictionary):
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False

if __name__ == '__main__':
    main()
