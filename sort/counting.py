# counting sort


# to sort only positive numbers
data = [1, 3, 4, 4, 3, 3, 3, 3, 2, 2,
        2, 2, 5, 3, 2, 4, 5, 3, 2, 1,
        3, 5, 2, 4, 3, 2, 5, 3, 4, 5,
        100, 34, 61, 57, 27, 9, 10, 10, 9, 0]

# test data for sorting data which includes negative numbers
data2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10,
         0, 2, 4, 1, 3, 7, 5, 6, 9, 10, 8]

def countingSort(data):
    mx, mn = abs(max(data)), abs(min(data))
    maxd = mx if mx >= mn else mn
    count = [0] * (maxd * 2 + 1)  # same as numpy.zeros()
    temp = []
    for i in data:  # count
        count[i + maxd] += 1
        print(f"{f'count[{i + maxd}] = {count[i + maxd]}': <50}// maxd : {maxd}, i : {i}")

    for i in range(maxd * 2 + 1):  # insert datas
        for _ in range(count[i]):
            temp.append(i - maxd)

    return temp  # return sorted data


# data = countingSort(data)
# print(data)

data2 = countingSort(data2)
print(data2)


