n = int(input())
cnt = 0
while True:
    if n == 1:
        print(cnt)
        break
    elif (n - 1) % 3 < n % 3 and (n - 1) % 2 < n % 2:
        n -= 1
    elif n % 3 == 0:
        n //= 3
    elif n % 2 == 0:
        n //= 2
    else:
        n -= 1
    cnt += 1
    print(n, cnt)


while True:
    if n == 1:
        print(cnt)
        break
    elif n % 6 == 0:
        while n != 1:
            n = n // 3 if n % 3 == 0 else n // 2
            cnt += 1
    else:
        print('Have to think more')

