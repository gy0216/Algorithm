import sys
import math

def main():
    numCases = int(sys.stdin.readline().rstrip())
    arr = [0] * (numCases+1)
    arr[1] = 0
    for i in range(2, numCases+1) :
        one = arr[i-1] +1

        if i %2 == 0 :
            two = arr[int(i/2)] +1
        else :
            two = 10000000
        
        if i%3 == 0 :
            three = arr[int(i/3)] +1
        else :
            three = 10000000

        min_n = min(one, two, three)

        arr[i] = min_n

    print(arr[numCases])

if __name__ == "__main__":
    main()