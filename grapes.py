import sys
import math

def main():
    num = int(sys.stdin.readline().rstrip())

    value = [0]
    
    for i in range(num):
        value.append(int(sys.stdin.readline().rstrip()))

    dp = [0] * (num+1)
    dp[1] = value[1]

    for i in range(2,num+1):
        if i ==2:
            dp[2] = value[1] + value[2]

        elif i==3:
            dp[3] = max(value[3]+value[1],value[3]+value[2],dp[i-1])

    for i in range(4,num+1):
        # print(i," ",dp[i-1])
        dp[i] = max(value[i]+value[i-1]+dp[i-3],value[i]+dp[i-2], dp[i-1])

    # print(dp)
    print(max(dp[num],dp[num-1]))

if __name__ == "__main__":
    main()