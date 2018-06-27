import sys

def found_fraction(num):
    
    count=1
    plus_count=4
    sum=1

    while sum<num:
        if(count%2!=0):
            sum += 1
            count+=1
        
        else:
            sum+=plus_count
            plus_count+=4
            count+=1
    # print("pc",plus_count)

    # print("sum",sum)
    # print("count",count)

    diff=abs(sum-num)
    # print("diff",diff)
    if diff >= count :
        sum = sum-plus_count+4
        diff= abs(sum-num)
        count-=1
        # print("afterdiff",diff)
    
    row = 1+diff
    col = count-diff

    return row,col


def main():
    number = int(sys.stdin.readline().rstrip())

    row,col = found_fraction(number)

    print(row,end="")
    print("/",end="")
    print(col)

if __name__ == "__main__":
    main()