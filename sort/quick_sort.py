def quickSort(xs):
    if len(xs) < 2:
        return xs
    else:
        pivot = xs[0]
        less = [value for value in xs[1:] if value <= pivot]
        greater = [value for value in xs[1:] if value > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
    
xs = [1, 6, 4, 2, 5, 9]

print(xs)
print(quickSort(xs[:]))
