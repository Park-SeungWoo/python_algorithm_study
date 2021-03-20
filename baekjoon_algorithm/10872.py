def factorial(i):
    if not 1 > i:
        return i * factorial(i - 1)
    else:
        return 1


n = int(input())
print(factorial(n))