import sys
import math

def main():
    num1 = int(sys.stdin.readline().rstrip())
    num2 = int(sys.stdin.readline().rstrip())

    count=0
    sum = 0
    min_num = num2
    for number in range(num1,num2+1):
        flag = 1

        if number == 1:
            continue
        for j in range(2,int(math.sqrt(number))+1):
            if number%j ==0:
                flag = 0
        
        if flag ==1:
            count+=1
            sum+=number
            if min_num > number:
                min_num = number

    if count==0 :
        print(-1)
    else :
        print(sum)
        print(min_num)
if __name__ == "__main__":
    main()