# bubble sort

def bubbleSort(arr):
    count = 0
    for i in arr:
        for jdx, j in enumerate(arr):
            if jdx < len(arr) - 1:
                if arr[jdx] > arr[jdx + 1]:
                    arr[jdx], arr[jdx + 1] = arr[jdx + 1], arr[jdx]
                    count += 1
                    print(count, arr)


arr = [2, 10, 5, 8, 7, 6, 4, 3, 1, 9]

print(arr)
bubbleSort(arr)
print(arr)
