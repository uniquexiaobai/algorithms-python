def mergeSort(xs):
    def _merge(left, right, merged):
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if (left[l] < right[r]):
                merged[l + r] = left[l]
                l += 1
            else:
                merged[l + r] = right[r]
                r += 1
        for l in range(l, len(left)):
            merged[l + r] = left[l]
        for r in range(r, len(right)):
            merged[l + r] = right[r]
        return merged
    def _mergeSort(xs):
        if len(xs) <= 1:
            return xs
        mid = len(xs) // 2
        left, right = _mergeSort(xs[:mid]), _mergeSort(xs[mid:])
        return _merge(left, right, xs[:])
    return _mergeSort(xs)

xs = [1, 6, 4, 2, 5, 9]

print(xs)
print(mergeSort(xs[:]))