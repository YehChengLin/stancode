"""
File: word_linked_list.py
Name:
----------------------------
This program demonstrates constructing
a character-based linked list from the word
input by user.
"""


class ListNode:
    def __init__(self, data, pointer):
        self.val = data
        self.next = pointer


def main():
    word = input('word: ')
    link_list = None
    for ch in word:
        new = ListNode(ch, None)
        if link_list is None:
            link_list = new
            cur = link_list
        else:
            cur.next = new
            cur = cur.next
    traversal(link_list)


def traversal(linked_list):
    cur = linked_list
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


if __name__ == '__main__':
    main()
