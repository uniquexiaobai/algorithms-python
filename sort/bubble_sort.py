def bubbleSort(xs):
    n = len(xs)
    isSorted = False
    for i in range(0, n - 1):
        if isSorted: break
        isSorted = True
        for j in range(0, n - i - 1):
            if xs[j] > xs[j + 1]:
                isSorted = False
                xs[j], xs[j + 1] = xs[j + 1], xs[j]
    return xs

xs = [1, 6, 4, 2, 5, 9]

print(xs)
print(bubbleSort(xs[:]))