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
            while fidx > 0 and data[fidx] > data[fidx - 1]:
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
    else:
        print("choose among 's' 'b' 'i' 'q'")

    print(f"{'after':=^40}\ndata => {a}")  # print test datas after sorted


def compareSortTime(a):
    sa = a.copy()
    ba = a.copy()
    ia = a.copy()
    qa = a.copy()

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

    print(f"{'result':=^40}")
    print(f"selection : {st}\nbubble : {bt}\ninsertion : {it}\nquick : {qt}")


if __name__ == '__main__':
    data = []  # to save random numeric data list from 1 to 5000
    for i in range(1000):  # append 5000 random numeric datas (accept redundancy)
        data.append(random.randrange(1, 5001))

    testd = [2, 1, 3, 6, 7, 9, 4, 5, 8, 10]
    testrd = [3, 1, 6, 2, 2, 3, 7, 9, 4, 5, 8, 10]  # easy-to-see test data

    a = data  # use 100 random data
    # a = testd  # use short test data
    # a = testrd  # use short test data (with redundancy)

    # chooseSortType(a, 'i')  # can see sorting process
    compareSortTime(a)  # can compare delay among sorting algorithms
