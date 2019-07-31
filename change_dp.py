# Uses python3

import sys

def get_change(money, coins):
    MinNumCoins = []
    for m in range(money + 1):
        MinNumCoins.append(m)
        for i in range(len(coins)):
            if m >= coins[i]:
                NumCoins = MinNumCoins[m - coins[i]] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m,[1,3,4]))
