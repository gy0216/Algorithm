import sys

numCases = sys.stdin.readline().rstrip().split(' ')

for i in range(3):
    numCases[i] = int(numCases[i])

arr = [[0]*(numCases[0]+1) for i in range(numCases[0]+1)]

for i in range(1, numCases[1]+1):
    num = sys.stdin.readline().rstrip().split(' ')
    num[0] = int(num[0])
    num[1] = int(num[1])
    arr[num[0]][num[1]] = 1
    arr[num[1]][num[0]] = 1
    
visited = [0] *( numCases[0]+1)


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

    
def DFS(startpoint):
    visited[startpoint] = 1

    print(startpoint, end=" ")

    for i in range(1, numCases[0]+1):
        if visited[i] == 0 and arr[startpoint][i] ==1:
            DFS(i)

def BFS(startpoint):
    visited[startpoint] = 1
    print(startpoint,end = " ")
    queue = Queue(numCases[0]+1)
    queue.push(startpoint)

    while(queue.isEmpty() == 0):
        tmp = queue.pop()

        for i in range(1,numCases[0]+1):
            if visited[i] == 0 and arr[tmp][i] ==1 :
                queue.push(i)
                visited[i] = 1
                print(i, end=" ")


def main():

    DFS(numCases[2])
    print()

    for i in range(0, numCases[0]+1):
        visited[i] = 0

    BFS(numCases[2])
    
if __name__ == "__main__":
    main()