# bubble sort


def bubbleSort(data):
    count = 0
    for idx, item in enumerate(data):  # sweep N times
        for jdx, jtem in enumerate(data):  # sweep
            if jdx < len(data) - 1 - idx and jtem > data[jdx + 1]:  # add the preceding condition to prevent access to sorted data
                data[jdx], data[jdx + 1] = data[jdx + 1], data[jdx]
                count += 1
                print(f"{f'step{count}': <10}{arr}")


arr = [2, 10, 5, 8, 7, 6, 4, 3, 1, 9]
a = [3, 1, 6, 2, 7, 9, 4, 5, 8, 10]

print(f"{'before':=^40}\n{a}")
bubbleSort(a)
print(f"{'after':=^40}\n{a}")
