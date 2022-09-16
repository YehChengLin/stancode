"""
File: priority_queue_linked_list.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


# It breaks the user inputs
EXIT = ''


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer


def main():
	priority_queue = None
	print('--------------------------------')
	while True:
		name = input('Patient: ')
		if name == EXIT:
			break
		pointer = int(input('Priority: '))
		data = (name, pointer)
		priority_queue1 = ListNode(data, None)
		if priority_queue is None:
			priority_queue = priority_queue1
		else:
			if priority_queue1.val[1] < priority_queue.val[1]:
				priority_queue1.next = priority_queue
				priority_queue = priority_queue1
			else:
				cur = priority_queue
				while cur is not None and cur.next is not None:
					if cur.val[1] <= priority_queue1.val[1] < cur.next.val[1]:
						priority_queue1.next = cur.next
						cur.next = priority_queue1
						break
					cur = cur.next
				cur.next = priority_queue1
				#if cur.val[1] <= priority_queue1.val[1]:
					#cur.next = priority_queue1
				#else:
					#cur = priority_queue
					#while cur is not None and cur.next is not None:
						#if cur.val[1] <= priority_queue1.val[1] < cur.next.val[1]:
							#priority_queue1.next = cur.next
							#cur.next = priority_queue1
							#break
						#cur = cur.next
	print('--------------------------------')
	traversal(priority_queue)


def traversal(priority_queue):
	"""
	:param priority_queue: ListNode, holding the first ListNode object 
						   as the start of priority queue
	--------------------------
	This function prints out each val of a linked list
	"""
	cur = priority_queue
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()
