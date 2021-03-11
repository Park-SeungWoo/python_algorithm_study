def selectionSort(data):
    for fidx, focus in enumerate(data):
        min = focus  # set focus
        midx = fidx
        for idx, i in enumerate(data):  # find minimum
            if min > i and idx >= fidx:  # idx must bigger than fidx
                min = i
                midx = idx

        data[fidx], data[midx] = data[midx], data[fidx]  # change focus, minimum data

        print(f"{f'step{fidx}': <10}{data}")  # print change logs


data = [3, 1, 6, 2, 7, 9, 4, 5, 8, 10]

print(f"{'before':=^40}\n{data}")
selectionSort(data)
print(f"{'after':=^40}\n{data}")

