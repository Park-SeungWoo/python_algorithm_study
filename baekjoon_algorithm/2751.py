import sys
import time
import random
sys.setrecursionlimit(10000)


def quickSort(data, start, end):
    if start >= end:
        return
    pivot = data[start]
    left = start + 1
    right = end
    while left <= right:
        while left <= end and pivot >= data[left]:
            left += 1
        while right > start and pivot < data[right]:
            right -= 1
        if left > right:
            data[right], data[start] = data[start], data[right]
        else:
            data[left], data[right] = data[right], data[left]

    quickSort(data, start, right - 1)
    quickSort(data, right + 1, end)


# try:
#     amount = int(input())
#     if not 1 <= amount <= 1000000:
#         raise Exception()
#     data = []
#     for i in range(amount):
#         ip = int(input())
#         if abs(ip) <= 1000000:
#             if ip not in data:
#                 data.append(ip)
#             else:
#                 raise Exception()
#         else:
#             raise Exception()
#
#     quickSort(data, 0, amount - 1)
#     for i in data:
#         print(i)
# except Exception:
#     print('close process')


d = []
for i in range(1000000):
    d.append(random.randrange(-1000000, 1000000))

s = time.time()
print(s)
quickSort(d, 0, 999999)
# d.sort()
e = time.time() - s
print(e)