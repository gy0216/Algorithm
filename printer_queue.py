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

    for i in range(numCases):
        num = sys.stdin.readline().rstrip().split(' ')
        num = [int(k) for k in num]

        queue = Queue(num[0] * num[0])
        priority = sys.stdin.readline().rstrip().split(' ')
        priority = [int(k) for k in priority]

        for j in range(num[0]):
            queue.push([j,priority[j]])

        count = 0
        while queue.isEmpty() == 0:
            start = queue.front+1
            max = queue.arrfront()
            # for q in range(start,start+queue.size()):
                # print("queue",queue.arr[q],end =" ")
            for p in range(start+1,start+queue.size()):
                if queue.arr[p][1] > max[1]:
                    max = queue.arr[p]
                    break

            v = queue.arrfront()

            if v[1] == max[1] :
                value = queue.pop()
                count+=1
                # print("count+")
                print("num",num[1])
                print("value",value[0])
                if value[0] == num[1]:
                    break
                
            else :
                # print("push")
                value = queue.pop()
                queue.push(value)

            # print()

        print(count)
                
            
if __name__ == "__main__":
    main()