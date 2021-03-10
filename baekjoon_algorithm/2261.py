import math
import numpy as np
import matplotlib.pyplot as plt


def minimumRoute(data, res, n, way):
    if n > len(data) - 2 or n + way > len(data) - 1:
        print(f"{f'pass': <60} // n : {n}, way : {way}, min : {res}")
        return res

    min = res
    # get distance
    if not data[n] == data[n + way]:
        dis = math.sqrt((data[n + way][0] - data[n][0]) ** 2 + (data[n + way][1] - data[n][1]) ** 2)
        min = dis if res > dis and way != 0 else res
        if not data[n] == data[n + way]:
            dist_dic[f'{data[n]}\n{data[n + way]}'] = dis
        print(f"{f'compare [{data[n]}, {data[n + way]}] : {dis}': <60} // n : {n}, way : {way}, min : {min}")

    # recursive
    min = minimumRoute(data, min, n, way + 1)
    min = minimumRoute(data, min, n + 1, way)

    return min


try:
    cnt = int(input())
    if not 2 <= cnt <= 100000:
        raise Exception()
    coords = []
    dist_dic = {}

    for _ in range(cnt):
        coord = list(map(int, input().split(' ')))
        for i in coord:
            if abs(i) > 10000:
                raise Exception()
        coords.append(coord)

    print(coords)

    min = minimumRoute(coords, float('inf'), 0, 0)

    # dist
    plt.figure(1)
    x = np.arange(len(dist_dic.keys()))
    plt.bar(x, list(dist_dic.values()))
    plt.xticks(x, list(dist_dic.keys()))
    for idx, i in enumerate(list(dist_dic.keys())):
        plt.text(idx, dist_dic[i], '%0.4f' % dist_dic[i], horizontalalignment='center')

    # coords
    plt.figure(2)
    x, y = zip(*coords)
    plt.scatter(x, y)
    plt.title('shortest distance algorithm')
    for coord in coords:
        plt.text(coord[0], coord[1], f'[{coord[0]}, {coord[1]}]')
    print(min)
    plt.show()
except:
    print('close process')


# solution (it works but failed in this test. I don't know the reason...)

# def minimumRoute(data, res, n, way):
#     if n > len(data) - 2 or n + way > len(data) - 1:
#         return res
#
#     min = res
#     # get distance
#     if not data[n] == data[n + way]:
#         dis = (data[n + way][0] - data[n][0]) ** 2 + (data[n + way][1] - data[n][1]) ** 2
#         min = dis if res > dis and way != 0 else res
#
#     # recursive
#     min = minimumRoute(data, min, n, way + 1)
#     min = minimumRoute(data, min, n + 1, way)
#
#     return min
#
#
# try:
#     cnt = int(input())
#     if not 2 <= cnt <= 100000:
#         raise Exception()
#     coords = []
#
#     for _ in range(cnt):
#         coord = list(map(int, input().split(' ')))
#         for i in coord:
#             if abs(i) > 10000:
#                 raise Exception()
#         coords.append(coord)
#
#     min = minimumRoute(coords, float('inf'), 0, 0)
#
#     print(min)
# except:
#     print('close process')
