import random
import time


class Sort:
    @staticmethod  # static method -> it can be called by its class name
    def selectionSort(data, t):
        print('selection sort')
        for idx, i in enumerate(data):
            min = i
            midx = idx
            for jdx, j in enumerate(data):  # find minimum
                if min > j and midx < jdx:
                    min = j
                    midx = jdx

            data[idx], data[midx] = data[midx], data[idx]  # swap
            if t:
                print(data)

    @staticmethod
    def bubbleSort(data, t):
        print('bubble sort')
        for idx, item in enumerate(data):
            for jdx, jtem in enumerate(data):
                if jdx < len(data) - 1 - idx and jtem > data[jdx + 1]:  # add the preceding condition to prevent access to sorted data
                    data[jdx], data[jdx + 1] = data[jdx + 1], data[jdx]
                    if t:
                        print(data)

    @staticmethod
    def insertionSort(data, t):
        print('insertion sort')
        for idx, _ in enumerate(data):
            fidx = idx
            while fidx > 0 and data[fidx] < data[fidx - 1]:
                data[fidx], data[fidx - 1] = data[fidx - 1], data[fidx]
                fidx -= 1
            if t:
                print(data)

    @classmethod  # class method -> it can access any methods or variables in this class using cls
    def quickSort(cls, data, t):
        print('quick sort')
        cls.quickRecursive(data, 0, len(data) - 1, t)

    @classmethod
    def quickRecursive(cls, data, start, end, t):
        if start >= end:
            return
        pivot = data[start]
        i = start + 1
        j = end

        while i <= j:
            while i <= end and pivot >= data[i]:
                i += 1
            while j > start and pivot <= data[j]:
                j -= 1
            if j < i:
                data[j], data[start] = data[start], data[j]
            else:
                data[i], data[j] = data[j], data[i]

            if t:
                print(data)

        cls.quickRecursive(data, start, j - 1, t)
        cls.quickRecursive(data, j + 1, end, t)

    @classmethod
    def mergeSort(cls, data):
        print('merge sort')
        cls.division(data, 0, len(data) - 1)

    @classmethod
    def division(cls, data, start, end):
        if end - start == 0:
            return

        mid = (start + end) // 2
        cls.division(data, start, mid)
        cls.division(data, mid + 1, end)
        cls.merge(data, start, mid, end)

    @classmethod
    def merge(cls, data, start, mid, end):
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


def chooseSortType(a, type):
    print(f"{'before':=^40}\ndata => {a}")  # print datas before sorted

    if type == 's':
        Sort.selectionSort(a, True)
    elif type == 'b':
        Sort.bubbleSort(a, True)
    elif type == 'i':
        Sort.insertionSort(a, True)
    elif type == 'q':
        Sort.quickSort(a, True)
    elif type == 'm':
        Sort.mergeSort(a)
    else:
        print("choose among 's' 'b' 'i' 'q' 'm'")

    print(f"{'after':=^40}\ndata => {a}")  # print test datas after sorted


def compareSortTime(a):
    sa = a.copy()
    ba = a.copy()
    ia = a.copy()
    qa = a.copy()
    ma = a.copy()

    st = time.time()
    Sort.selectionSort(sa, False)
    st = time.time() - st

    bt = time.time()
    Sort.bubbleSort(ba, False)
    bt = time.time() - bt

    it = time.time()
    Sort.insertionSort(ia, False)
    it = time.time() - it

    qt = time.time()
    Sort.quickSort(qa, False)
    qt = time.time() - qt

    mt = time.time()
    Sort.mergeSort(ma)
    mt = time.time() - mt

    print(f"{'result':=^40}")
    print(f"selection : {st}\nbubble : {bt}\ninsertion : {it}\nquick : {qt}\nmerge : {mt}")


if __name__ == '__main__':
    data = []  # to save random numeric data list from 1 to 5000
    for i in range(10000):  # append 5000 random numeric datas (accept redundancy)
        data.append(random.randrange(1, 5001))

    testd = [2, 1, 3, 6, 7, 9, 4, 5, 8, 10]
    testrd = [3, 1, 6, 2, 2, 3, 7, 9, 4, 5, 8, 10]  # easy-to-see test data
    alsorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    a = data  # use 100 random data
    # a = testd  # use short test data
    # a = testrd  # use short test data (with redundancy)
    # a = alsorted  # test with already sorted data

    # chooseSortType(a, 'm')  # can see sorting process
    compareSortTime(a)  # can compare delay among sorting algorithms
