import sys
import math

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.arr = [0] * capacity

    def push(self, num):
        self.arr[self.top] = num
        self.top+=1
    
    def pop(self):
        if self.top == 0:
            return -1
        else:
            self.top -= 1
            return self.arr[self.top]

    def size(self):
        return self.top
    
    def isEmpty(self):
        if self.top == 0 :
            return 1
        else :
            return 0
    
    def arrtop(self):
        if self.top == 0:
            return -1
        else :
            return self.arr[(self.top)-1]
    

def main():
    numCases = int(sys.stdin.readline().rstrip())
    stack = Stack(numCases)

    arr = []

    for i in range(1,numCases+1):
        arr.append(int(sys.stdin.readline().rstrip()))

    sequence = []
    count=0

    for i in range(1,numCases+1):
        stack.push(i)
        sequence.append('+')

        while stack.isEmpty()!=1 and stack.arrtop() == arr[count] :
            stack.pop()
            sequence.append('-')
            count+=1
            
    if stack.isEmpty() == 0 :
        print("NO")
    else :
        for i in sequence: print(i)
        



        
        
            
if __name__ == "__main__":
    main()