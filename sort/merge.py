# merge sort
import random


def mergeSort(data, start, end):
    if end - start == 0:  # if length of data is 1
        # print(f"start : {data[start]}, end : {data[end]}")
        return

    mid = (start + end) // 2
    mergeSort(data, start, mid)  # from start to middle
    mergeSort(data, mid + 1, end)  # from middle to end
    merge(data, start, end)


def merge(data, start, end):
    # left : start to mid
    # right : mid + 1 to end
    # index : to save sorted data
    temp = []  # to save temporarily sorted data list
    mid = (start + end) // 2
    left, right, index = start, mid + 1, start
    while left <= mid and right <= end:
        if data[left] < data[right]:
            temp.append(data[left])
            left += 1
        else:
            temp.append(data[right])
            right += 1

    # append remaining datas after do preceding process
    # <example>
    # [3] [1] [(temp)] (left == 0, right == 1, mid == 0)
    # [3] [] [1] (left == 0, right == 2, mid == 0)
    # process end
    # 3 is remaining element so, we have to append it.
    if left <= mid:
        for i in data[left:mid + 1]:  # add remaining left ~ mid data
            temp.append(i)
    else:
        for i in data[right:end + 1]:  # add remaining right ~ end data
            temp.append(i)

    # print(f"{f'{temp}': <50}// start : {start}, end : {end}, left : {left}, right : {right}")

    for item in temp:
        data[index] = item
        index += 1


# usage
dataset = [3, 1, 6, 2, 7, 9, 4, 5, 8, 10]
rdataset = []
for _ in range(1000):
    rdataset.append(random.randrange(1000))

btn = True  # True : short dataset, False : random 1000 dataset

testdata = dataset if btn else rdataset

print(f"{'before':=^40}\n{testdata}")
mergeSort(testdata, 0, len(testdata) - 1)
print(f"{'after':=^40}\n{testdata}")
