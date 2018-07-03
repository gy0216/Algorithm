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

    for i in range(0, numCases):
        case = sys.stdin.readline().rstrip().split(' ')
        if case[0] == 'push':
            case[1] = int(case[1])
            
            stack.push(case[1])
        
        elif case[0] == 'pop':
            re = stack.pop()
            print(re)
        
        elif case[0] == 'size':
            re = stack.size()
            print(re)

        elif case[0] == 'empty':
            re = stack.isEmpty()
            print(re)
        
        elif case[0] == 'top':
            re = stack.arrtop()
            print(re)
        
            
if __name__ == "__main__":
    main()