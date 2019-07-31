# Uses python3


import sys

def get_change(m):
    #write your code here
    change = 0
    while m >= 10:
        change = change + 1
        m = m - 10
    while 5 <= m < 10:
        change = change + 1
        m = m - 5
    while m < 5 and m != 0:
        change = change + 1
        m = m - 1
    if m == 0:
        return change

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
