def binarySearch(list, target):
	l = 0
	r = len(list) - 1

	while l <= r:
		mid = (l + r) >> 1

		if target < list[mid]:
			r = mid - 1
		elif target > list[mid]:
			l = mid + 1
		else:
			return mid

	return None

list = [1, 3, 5, 7, 9]

print(binarySearch(list, 7))
