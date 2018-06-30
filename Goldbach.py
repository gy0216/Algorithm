import sys
import math

def main():
    numCases = int(sys.stdin.readline().rstrip())
   
    num_arr = []
    for i in range(0,numCases) :
        num_arr.append(int(sys.stdin.readline().rstrip()))

    for number in num_arr:
        for num1 in range(int(number/2),1,-1) :

            flag1 = 1
            flag2 = 1
            for j in range(2,int(math.sqrt(num1))+1):
                if num1 % j == 0:
                    flag1 =0
                    continue
                
            if flag1 ==1 :
                num2 = number-num1
                for j in range(2, int(math.sqrt(num2))+1):
                    if num2 % j ==0:
                        flag2 =0
                        continue
                
                if flag2 == 1:
                    print(num1,num2)
                    break
            
            
if __name__ == "__main__":
    main()