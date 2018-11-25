def insertionSort(xs):
    n = len(xs)
    for i in range(1, n):
        x = xs[i]
        j = i - 1
        while j >= 0 and xs[j] > x:
            xs[j + 1] = xs[j]
            j -= 1
        xs[j + 1] = x
    return xs

def instertionSortWithBinarySearch(xs):
	n = len(xs)
	for i in range(1, n):
		x = xs[i]
		p = binarySearch(xs[:i], x)
		for j in range(i, p, -1):
			xs[j] = xs[j - 1]
		xs[p] = x
	return xs;

def binarySearch(xs, x):
	l = 0
	r = len(xs) - 1
	while (l <= r):
		mid = (l + r) // 2
		if x == xs[mid]:
			return mid
		elif x > xs[mid]:
			l = mid + 1
		else:
			r = mid - 1
	return l

xs = [1, 4, 9, 2, 7, 5]
print(xs)
print(insertionSort(xs[:]))
print(instertionSortWithBinarySearch(xs))
