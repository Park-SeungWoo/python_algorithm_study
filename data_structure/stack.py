import os
import time


class stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        # self.data.pop()
        del self.data[len(self.data) - 1]

    def print(self):
        for item in self.data[::-1]:
            print(f"|{f'{item}': ^5}|")
        print('-------')


os.system('clear')

stackdata = stack()
for i in range(10):
    print('push', i + 1)
    stackdata.push(i + 1)
    stackdata.print()
    time.sleep(1)
    os.system('clear')

for i in stackdata.data[::-1]:
    print('pop', i)
    stackdata.pop()
    stackdata.print()
    time.sleep(1)
    os.system('clear')