import sys
import math

def main():
    num = int(sys.stdin.readline().rstrip())
    num_list = sys.stdin.readline().rstrip().split(' ')

    count=0
    for i in num_list:
        flag = 1
        number = int(i)

        if number == 1:
            continue
        for j in range(2,int(math.sqrt(number))+1):
            if number%j ==0:
                flag = 0
        
        if flag ==1:
            count+=1

    print(count)
    
if __name__ == "__main__":
    main()