# Uses python3

import sys
import numpy as np

def optimal_weight(W, w, n):
    # write your code here
    d = np.zeros((n + 1, W + 1))
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            d[i, j] = d[i - 1, j]
            if w[i - 1] <= j:
                val = d[i - 1, j - w[i - 1]] + w[i - 1]
                if d[i, j] < val:
                    d[i, j] = val
    return int(d[n, W])

def optimal_weight2(W, w, n):
    dp_result = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(1, n+1):
        for weight in range(1, W+1):
            dp_result[i][weight] = dp_result[i-1][weight]
            if w[i-1] <= weight:
                val = dp_result[i-1][weight - w[i-1]] + w[i-1]
                if val > dp_result[i][weight]:
                    dp_result[i][weight] = val
            print('i, j: ', i, weight)
            #print('val: ', val)
            print('w[i]: ', w[i - 1])
            print(*dp_result)
    return int(dp_result[n][W])

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))
