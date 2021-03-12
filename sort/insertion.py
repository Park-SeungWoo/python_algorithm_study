# insertion


def insertionSort(data):
    for idx, _ in enumerate(data):
        fidx = idx  # focus on Nth element
        while fidx > 0 and data[fidx] > data[fidx - 1]:  # sweep elements in left side of focus
            data[fidx], data[fidx - 1] = data[fidx - 1], data[fidx]  # insertion like bubble sort
            fidx -= 1
        print(f"{f'step{idx}': <10}{data}")


a = [3, 1, 6, 2, 7, 9, 4, 5, 8, 10]

print(f"{'before':=^40}\n{a}\n")
insertionSort(a)
print(f"{'after':=^40}\n{a}")
