import random
import time


a = int(input())
st = time.time()
d = [0] * 2000001
for _ in range(a):
    i = random.randrange(-1000000, 1000000)
    d[i + 1000000] += 1

for i in range(a):
    for _ in range(d[i]):
        print(d[i] - 1000000)
et = time.time() - st
print(et)
