# counting sort


r = 100  # range of numbers(1 ~ 5)
data = [1, 3, 4, 4, 3, 3, 3, 3, 2, 2,
        2, 2, 5, 3, 2, 4, 5, 3, 2, 1,
        3, 5, 2, 4, 3, 2, 5, 3, 4, 5,
        100, 34, 61, 57, 27, 9, 10, 10, 9, 27]


def countingSort(data, r):
    count = [0] * r  # same as numpy.zeros(r)
    temp = []
    for i in data:
        count[i - 1] += 1

    for i in range(r):
        for j in range(count[i]):
            temp.append(i + 1)

    return temp


data = countingSort(data, r)
print(data)
