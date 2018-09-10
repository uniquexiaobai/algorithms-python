def binarySearch(xs, target):
	l = 0
	r = len(xs) - 1
	while l <= r:
		mid = (l + r) >> 1
		if target < xs[mid]:
			r = mid - 1
		elif target > xs[mid]:
			l = mid + 1
		else:
			return mid
	return None

xs = [1, 3, 5, 7, 9]
print(binarySearch(xs, 7))
