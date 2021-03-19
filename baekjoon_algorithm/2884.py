h, m = map(int, input().split(' '))
hours = [i for i in range(24)]  # [0, ~, 23]

if m - 45 < 0:
    h = hours[h - 1]  # if h == 0 => hours[h - 1] == 23
    m += 15  # 60 + (m - 45)
else:
    m -= 45

print(h, m)