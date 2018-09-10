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

xs = [1, 4, 9, 2, 7, 5]

print(xs)
print(insertionSort(xs[:]))
