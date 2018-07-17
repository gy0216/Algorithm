import sys
import math

def main():
    numCases = int(sys.stdin.readline().rstrip())
    arr = [[0] * numCases for i in range(11)]

    for i in range(1,10):
        arr[i][0] = 1
    arr[10][0] = 9

    for i in range(1,numCases):
        sum = 0
        for j in range(10):
            if j == 0 :
                arr[0][i] = arr[1][i-1]
            elif j == 9 :
                arr[9][i] = arr[8][i-1]
            else :
                arr[j][i] = arr[j+1][i-1] + arr[j-1][i-1]
            
            sum += arr[j][i]
        
        arr[10][i] = sum
    
    print(arr[10][numCases-1]%1000000000)

if __name__ == "__main__":
    main()