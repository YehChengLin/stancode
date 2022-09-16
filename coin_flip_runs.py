"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random



def main():
	"""
	TODO:
	"""
	print("Let's flip a coin!")
	n = int(input('Number of runs: '))
	run = 0
	c = False
	a = random.randrange(1, 3)
	if a == 1:
		print('H', end='')
	else:
		print('T', end='')
	while True:
		b = random.randrange(1, 3)
		if a == b:
			if not c:
				run += 1
				c = True
		else:
			c = False
		if b == 1:
			print('H', end='')
		else:
			print('T', end='')
		a = b
		if n == run:
			break


















# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
