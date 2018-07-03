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
    arr = sys.stdin.readline().rstrip()

    stack = Stack(len(arr))
        
    for i in arr:
        sum = 0
        if i =='(':
            stack.push(i)
        elif i == ')' :
            if stack.arrtop() == '(':
                stack.pop()
                stack.push(2)
                continue

            while type(stack.arrtop())==int and stack.arrtop()!=-1 :
                sum+= stack.arrtop()
                stack.pop()
                    
            if stack.arrtop() == '(':
                sum = sum*2
                stack.pop()
                stack.push(sum)
            else :
                break

        elif i =='[':
            stack.push(i)
        elif i == ']' :
            if stack.arrtop() == '[':
                stack.pop()
                stack.push(3)
                continue

            while type(stack.arrtop())==int and stack.arrtop()!=-1:
                sum+=stack.arrtop()
                stack.pop()
                    
            if stack.arrtop() == '[':
                sum = sum*3
                stack.pop()
                stack.push(sum)
            else :
                break

    result = 0
    for i in range(0,stack.top):
        if type(stack.arrtop()) == int :
            result += stack.arrtop()
            stack.pop()
        else :
            break

    if stack.isEmpty() ==1 :
        print(result)

    else:
        print(0)
    
if __name__ == "__main__":
    main()