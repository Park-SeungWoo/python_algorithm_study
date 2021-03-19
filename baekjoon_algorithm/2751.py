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


def mergeSort(data, start, end):
    if end - start == 0:
        return

    mid = (start + end) // 2
    mergeSort(data, start, mid)
    mergeSort(data, mid + 1, end)
    merge(data, start, mid, end)


def merge(data, start, mid, end):
    left = start
    right = mid + 1
    index = start
    temp = []
    while left <= mid and right <= end:
        if data[left] > data[right]:
            temp.append(data[right])
            right += 1
        else:
            temp.append(data[left])
            left += 1

    if left > mid:
        for item in data[right: end + 1]:
            temp.append(item)
    else:
        for item in data[left: mid + 1]:
            temp.append(item)

    for item in temp:
        data[index] = item
        index += 1


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
#     mergeSort(data, 0, amount - 1)
#     for i in data:
#         print(i)
# except Exception:
#     print('close process')


qd = []
for i in range(1000000):
    qd.append(random.randrange(-1000000, 1000000))

md = qd.copy()

qs = time.time()
quickSort(qd, 0, len(qd) - 1)
qe = time.time() - qs

ms = time.time()
mergeSort(md, 0, len(md) - 1)
me = time.time() - ms

print(f"quick : {qe}\nmerge : {me}")