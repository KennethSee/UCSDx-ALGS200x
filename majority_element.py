# Uses python3

import sys
import math

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    a.sort()
    #for i in range(right):
    #    #print(a[i])
    #    counter = 0
    #    for j in range(right):
    #        if a[i] == a[j]:
    #            counter += 1
    #    if counter > n/2:
    #        return counter
    #for i in range(right):
        #adder = 1
        #counter = 1
        #if i < right and i + adder < right:
        #    while a[i] == a[i + adder]:
        #        #print('number: ', a[i], a[i + adder])
        #        #print('counter: ', counter)
        #        counter += 1
        #        adder += 1
        #        if i + adder >= right:
        #            break
        #if counter > n/2:
        #    return counter
    for pos in range(right):
        if pos + math.ceil((right - 1)/2) < right:
             if a[pos] == a[pos + math.ceil((right - 1)/2)]:
                 return 1
        elif pos > math.ceil((right - 1)/2):
             return -1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #print(*a)
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
