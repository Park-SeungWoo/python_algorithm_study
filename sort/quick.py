# quick sort


def quickSort(arr, start, end):
    if start >= end:
        return

    pivot = start
    i = start + 1
    j = end

    while i <= j:
        while i <= end and arr[pivot] <= arr[i]:
            i += 1
        while j > start and arr[pivot] >= arr[j]:
            j -= 1

        if i > j:
            arr[j], arr[pivot] = arr[pivot], arr[j]
        else:
            arr[i], arr[j] = arr[j], arr[i]

        print(arr)

    quickSort(arr, start, j - 1)
    quickSort(arr, j + 1, end)



# use


data = [3, 7, 5, 6, 8, 2, 1, 4, 9, 10]

print(f"{'before':=^40}\n{data}\n")
quickSort(data, 0, len(data) - 1)
print(f"{'after':=^40}\n{data}\n")

