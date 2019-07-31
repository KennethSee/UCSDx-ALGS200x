# Uses python3

import sys
import math

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def binary_search(a, left, right, x):
    # write your code here
    while right >= left:
        mid = left + int((right-left)/2)
        #print('left: ', left)
        #print('right: ', right)
        #print('testmid: ', mid)
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            return binary_search(a, left, mid - 1, x)
        else:
            return binary_search(a, mid + 1, right, x)
    #try:
    #    if a[left] == len(a) - 1:
    #        return left
    #    return -1
    #except:
    #    return -1
    return -1

def linear_search(a, left, right, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n]
    a = data[1:n+1]
    left, right = 0, len(a) - 1
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
	    print(binary_search(a, left, right, x), end = ' ')
