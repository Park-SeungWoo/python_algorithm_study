def factorial(i):
    if not 1 > i:
        return i * factorial(i - 1)
    else:
        return 1


try:
    n = int(input())
    if not 0 <= n <= 12:
        raise Exception()
    print(factorial(n))
except Exception:
    print('err')
