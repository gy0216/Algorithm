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

    for i in range(0,numCases):
        arr =  sys.stdin.readline().rstrip()
        stack = Stack(len(arr))
        
        for i in arr:
            if i =='(':
                stack.push(i)
            elif i == ')' :
                if stack.arrtop() == '(' :
                    stack.pop()
                else :
                    stack.push(i)
                    break
            
        if stack.isEmpty() == 1 :
            print('YES')
        else:
            print('NO')
        



        
        
            
if __name__ == "__main__":
    main()