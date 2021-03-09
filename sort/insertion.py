# insertion

import random


def insertionSort(arr):
    cnt = 1
    for idx, i in enumerate(arr):
        if idx > 0:
            sdx = idx
            while sdx >= 0:
                if sdx > 0 and arr[sdx] < arr[sdx - 1]:
                    arr[sdx], arr[sdx - 1] = arr[sdx - 1], arr[sdx]
                    print(arr)
                sdx -= 1
                print(cnt)
                cnt += 1


# arr = [1, 3, 4, 6, 8, 9, 7, 10, 2, 5, 12, 43, 65, 73, 67, 2, 6, 45, 78, 68, 300, 200956, 28, 48, 6, 345]
#
# print(f"{'before':=^40}\n{arr}\n")
# insertionSort(arr)
# print(f"{'after':=^40}\n{arr}")

def randomArr():
    arr = []
    for i in range(1000):
        arr.append(random.randrange(0, 1000))
    return arr


a= randomArr()
b = a.copy()
print(f"{'before':=^40}\n{a}\n")
insertionSort(a)
print(f"{'after':=^40}\n{a}")

print(b)
b.sort()
print(b)