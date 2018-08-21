def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [value for value in arr[1:] if value <= pivot]
        greater = [value for value in arr[1:] if value > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
    
list = [1, 6, 4, 2, 5, 9]

print(list)
print(quickSort(list[:]))
