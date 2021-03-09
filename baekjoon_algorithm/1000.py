try:
    a, b = map(int, input().split(' '))
    if a <= 0 or b >= 10:
        raise Exception()
    else:
        print(a + b)
except Exception:
    print('exit')