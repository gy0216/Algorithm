import sys

def one_number(n):
    if n<100:
        return n

    else:
        sum = 99
        for i in range(100,n+1):
            # print("i",i)
            result = 1
            num = i
            f_num = num%10
            num = int(num/10)
            s_num = num%10
            # print(f_num," ",num," ",s_num)

            while int(num/10)!=0:
                f_minus = f_num-s_num
                
                f_num = s_num
                num = int(num/10)
                s_num = num%10

                s_minus = f_num-s_num
                # print(f_num," ",num," ",s_num)

                if f_minus != s_minus:
                    result = 0
                    break

            if result ==1:
                sum+=1
                # print("sum",sum)
            
        return sum

    
def main():
   a = int(sys.stdin.readline().rstrip())

   result = one_number(a)
   print(result)

if __name__ == "__main__":
    main()