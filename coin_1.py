import sys
import math

def main():
    num = list(map(int,sys.stdin.readline().rstrip().split()))
    coins = [0]

    for i in range(num[0]):
        coins.append(int(sys.stdin.readline().rstrip()))
    
    dp = [[0] * (num[1] +1) for i in range(num[0]+1)]
    
    for i in range(num[1]+1):
        dp[0][i] = 0

    for i in range(num[0]+1):
        dp[i][0] = 1

    for i in range(1,num[1]+1):
        for j in range(1,num[0]+1):
            if i - coins[j] >= 0 :
                dp[j][i] = dp[j-1][i] + dp[j][i-coins[j]]
            else : 
                dp[j][i] = dp[j-1][i]
    
    print(dp[num[0]][num[1]])
    print(dp)

if __name__ == "__main__":
    main()