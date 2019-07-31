# Uses python3

import sys

def best_item(n, w, v):
    maxValuePerWeight = 0
    bestItem = 0
    for i in range(n):
        if w[i] > 0:
             if v[i]/w[i] > maxValuePerWeight:
                 maxValuePerWeight = v[i]/w[i]
                 bestItem = i
    # print(bestItem)
    return bestItem

def get_optimal_value(n, capacity, weights, values):
    value = 0.
    #item_value = []
    for i in range(n):
        if capacity == 0:
             return value
        j = best_item(n, weights, values)
        # print(weights[j])
        a = min(weights[j], capacity)
        value = value + a * (values[j]/weights[j])
        weights[j] = weights[j] - a
        # print(weights[j])
        capacity = capacity - a
        # print(capacity)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))
