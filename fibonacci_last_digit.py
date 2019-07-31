#using python3


import sys

def get_fibonacci_last_digit_naive(n):
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
    	f.append((f[i-1]+f[i-2])%10)
    return f[n]


# input = sys.stdin.read()
n = int(input())
print(get_fibonacci_last_digit_naive(n))
