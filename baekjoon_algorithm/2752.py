arr = list(map(int, input().split(' ')))
for idx, _ in enumerate(arr):
    midx = idx
    while midx > 0 and arr[midx] < arr[midx - 1]:
        arr[midx], arr[midx - 1] = arr[midx - 1], arr[midx]
        midx -= 1
for i in arr:
    print(i, end=' ')