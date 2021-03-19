import os
import time


class queue:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        del self.data[0]

    def print(self):
        print(self.data)


os.system('clear')
qdata = queue()

for i in range(10):
    print('push ', i + 1)
    qdata.push(i + 1)
    qdata.print()
    time.sleep(1)
    os.system('clear')

for i in qdata.data[:]:
    print('pop', i)
    qdata.pop()
    qdata.print()
    time.sleep(1)
    os.system('clear')