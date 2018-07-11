import sys
import math

def main():
    numCases = int(sys.stdin.readline().rstrip())
    arr =[0] * numCases 
    for i in range(numCases):
        arr[i] = int(sys.stdin.readline().rstrip())
    
    value = [0]* numCases
    value[0] = arr[0]
    value[1] = arr[0] + arr[1]
    for i in range(2, numCases):
        min_value = max(arr[i-1]+value[i-3], value[i-2])

        value[i] = arr[i]+min_value

    print(value[numCases-1])


if __name__ == "__main__":
    main()