import sys

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.arr = [0] * capacity

    def push(self, num):
        self.rear+=1
        self.arr[self.rear] = num
    
    def pop(self):
        if self.front == self.rear:
            return -1
        else:
            self.front += 1
            return self.arr[self.front]

    def size(self):
        return self.rear - self.front
    
    def isEmpty(self):
        if self.rear == self.front :
            return 1
        else :
            return 0
    
    def arrfront(self):
        if self.rear == self.front:
            return -1
        else :
            return self.arr[(self.front)+1]

    def back(self):
        if self.rear == self.front:
            return -1
        else :
            return self.arr[(self.rear)]
    

def main():
    numCases = int(sys.stdin.readline().rstrip())
    queue = Queue(numCases)

    for i in range(0, numCases):
        case = sys.stdin.readline().rstrip().split(' ')
        if case[0] == 'push':
            case[1] = int(case[1])
            
            queue.push(case[1])
        
        elif case[0] == 'pop':
            re = queue.pop()
            print(re)
        
        elif case[0] == 'size':
            re = queue.size()
            print(re)

        elif case[0] == 'empty':
            re = queue.isEmpty()
            print(re)
        
        elif case[0] == 'front':
            re = queue.arrfront()
            print(re)
            
        elif case[0] == 'back':
            re = queue.back()
            print(re)

            
if __name__ == "__main__":
    main()