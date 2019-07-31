# Uses python3

import sys

def get_change(money, coins):
    #write your code here
    MinNumCoins = []
    for m in range(money + 1):
        MinNumCoins.append(m)
        for i in range(len(coins)):
            if m >= coins[i]:
                NumCoins = MinNumCoins[m - coins[i]] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
        #print('m: ', m)
        #print('MinNumCoins: ', MinNumCoins[m])
    return MinNumCoins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = 6
    print(get_change(m,[1,3,4]))
