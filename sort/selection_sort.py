def selectionSort(xs):
    for i in range(0, len(xs) - 1):
        minIndex = i
        for j in range(i + 1, len(xs)):
            if xs[j] < xs[minIndex]:
                minIndex = j
        if minIndex != i:
            xs[minIndex], xs[i] = xs[i], xs[minIndex]
    return xs

xs = [3, 6, 4, 2, 9]

print(xs)
print(selectionSort(xs[:]))
