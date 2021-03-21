import random
import time


def countingSort(data):
    mx, mn = abs(max(data)), abs(min(data))
    maxd = mx if mx >= mn else mn
    count = [0] * (maxd * 2 + 1)
    temp = []  # delete when you submit
    for i in data:
        count[i + maxd] += 1

    for i in range(maxd * 2 + 1):
        for _ in range(count[i]):
            # print(i - maxd)
            temp.append(i - maxd)  # delete when you submit

    return temp  # delete when you submit


# amount = int(input())
# data = []
# for i in range(amount):
#     ip = int(input())
#     data.append(ip)
#
# countingSort(data)


cd = []
for i in range(1000000):
    cd.append(random.randrange(-1000000, 1000000))

cs = time.time()
cd = countingSort(cd)
ce = time.time() - cs

print(ce)