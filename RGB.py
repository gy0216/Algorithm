import sys

def main():
    arr = []
    numCases = int(sys.stdin.readline().rstrip())
    for i in range(numCases):
        arr.append(sys.stdin.readline().rstrip().split(' '))
        for j in range(3) :
            arr[i][j] = int(arr[i][j])
    
    for i in range(1,numCases):
        arr[i][0] = arr[i][0] + min(arr[i-1][1], arr[i-1][2])
        arr[i][1] = arr[i][1] + min(arr[i-1][0], arr[i-1][2])
        arr[i][2] = arr[i][2] + min(arr[i-1][0], arr[i-1][1])
    print(min(arr[numCases-1]))

    


if __name__ == "__main__":
    main()