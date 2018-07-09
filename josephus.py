import sys
import math

class Queue:
    def __init__(self, capacity):
        self.maxsize = capacity
        self.front = 0
        self.rear = 0
        self.arr = [0] * self.maxsize

    def isFull(self):
        if self.front == (self.rear +1) % self.maxsize :
            return 1
        else :
            return 0
    
    def isEmpty(self):
        if self.front == self.rear :
            return 1
        else :
            return 0

    def enqueue(self, num):
        if self.isFull() == 1:
            return -1
        else :
            self.rear = self.rear+1
            self.rear = self.rear % self.maxsize

            self.arr[self.rear] = num

    def dequeue(self):
        if self.isEmpty() ==1:
            return -1
        else :
            self.front = self.front+1
            self.front = self.front % self.maxsize

            return self.arr[self.front]

    def size(self):
        if self.rear > self.front :
            return self.rear - self.front
        else :
            return self.maxsize - abs(self.rear-self.front)

def main():
    numCases = sys.stdin.readline().rstrip().split(' ')
    numCases = [int(numCases[i]) for i in range(len(numCases))]

    queue = Queue(numCases[0]+1)

    for i in range(1, numCases[0]+1) :
        queue.enqueue(i)

    strarr ="<"
    while True:
        # print("f",queue.front)
        # print("r",queue.rear)
        if queue.size() == 1 :
            strarr+=str(queue.dequeue())
            break
        for i in range(numCases[1]-1):
            pindex = queue.dequeue()
            # print("ppppp",pindex)
            queue.enqueue(pindex)
        
        pindex = queue.dequeue()
        strarr+=str(pindex)
        strarr+=(", ")
    
    strarr+=(">")

    print(strarr)

if __name__ == "__main__":
    main()