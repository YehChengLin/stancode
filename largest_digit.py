"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""



def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	if 0 < n < 10:
		return n
	else:
		if n > 0:
			a = n % 10
			n2 = find_largest_digit(n//10)
			if a > n2:
				return a
			else:
				return n2
		if n < 0:
			n = n * -1
			b = n % 10
			n3 = find_largest_digit(n // 10)
			if b > n3:
				return b
			else:
				return n3















if __name__ == '__main__':
	main()
