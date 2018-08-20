def selectionSort(arr):
    arr = arr[:]

    for i in range(0, len(arr) - 1):
        minIndex = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        if minIndex != i:
            arr[minIndex], arr[i] = arr[i], arr[minIndex]

    return arr

list = [3, 6, 4, 2, 9]

print(list)
print(selectionSort(list))
