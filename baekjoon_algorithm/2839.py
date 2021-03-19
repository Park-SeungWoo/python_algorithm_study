# def leastPb(n):
#     count = 0
#     while n:
#         if n % 5 != 0 and n % 3 == 0:
#             n -= 3
#             count += 1
#         elif n >= 5:
#             n -= 5
#             count += 1
#         else:
#             print(-1)
#             return
#     print(count)
#
#
# amount = int(input())
# leastPb(amount)


amount = int(input())
count = 0
while True:
    if amount % 5 != 0 and amount % 3 == 0:
        amount -= 3
        count += 1
    elif amount >= 5:
        amount -= 5
        count += 1
    elif amount == 0:
        print(count)
        break
    else:
        print(-1)
        break
