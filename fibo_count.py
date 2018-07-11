import sys

arr=[0] * 43

def fibo(n):
    if n<=1 :
        return arr[n]
    else :
        if arr[n] >0 :
            return arr[n]
    arr[n] =fibo(n-1)+fibo(n-2)
    return arr[n]



def main():
    numCases = int(sys.stdin.readline().rstrip())
    arr[0] = arr[1] =1

    for i in range(numCases):
        num = int(sys.stdin.readline().rstrip())

        if num ==0 : 
            print("1 0")
        elif num ==1 : 
            print("0 1")
        else :
            fibo(num)
            print(arr[num-2],arr[num-1])

if __name__ == "__main__":
    main()