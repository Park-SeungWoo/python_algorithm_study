# quick sort


def quickSort(arr, start, end):
    if start >= end:  # if len(data) == 1 or start and end are crossed
        return

    pivot = start  # pivot = first element in data set
    i = start + 1  # find i bigger than pivot from start to right
    j = end  # find j smaller than pivot from end to left

    while i <= j:  # do the process until i, j are crossed
        while i <= end and arr[pivot] >= arr[i]:  # find bigger than pivot
            i += 1
        while j > start and arr[pivot] <= arr[j]:  # find smaller than pivot
            j -= 1

        if i > j:  # if crossed, change pivot, smaller element
            arr[j], arr[pivot] = arr[pivot], arr[j]
        else:  # else, change bigger, smaller element
            arr[i], arr[j] = arr[j], arr[i]

        print(arr)  # change log

    # recursion
    quickSort(arr, start, j - 1)  # do the same process in left side data set of pivot
    quickSort(arr, j + 1, end)  # do the same process in right side data set of pivot


# use
data = [6, 1, 5, 7, 4, 8, 3, 9, 2, 10, 6]

print(f"{'before':=^40}\n{data}\n")
quickSort(data, 0, len(data) - 1)
print(f"{'after':=^40}\n{data}\n")

