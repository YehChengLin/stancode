def main():
	lst = [3, 6, 9, 10, 11, 23, 33, 45, 66, 99]
	print(binary_search(lst, 7))
	print(binary_search(lst, 23))


def binary_search(lst, target):
	"""
	:param lst: list[int], a Python list storing integers.
	:param target: int, the value to be searched.
	:returns : bool, if target is in the lst or not.
	"""
	# Your Code Here
	return helper(lst, target, len(lst)//2)


def helper(lst, target, mid):
	if lst[mid] == target:
		return True
	else:
		if lst[mid] > target:
			new_lst = lst[:mid]
		else:
			new_lst = lst[mid+1:]
		if len(new_lst) == 0:
			return False
	return helper(new_lst, target, len(new_lst)//2)


if __name__ == '__main__':
	main()
