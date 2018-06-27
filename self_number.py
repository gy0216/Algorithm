def self_num(n):
    sum = n
    while True:

        if n/10 ==0:
            sum += n
            break

        sum += n%10
        n = int(n/10)
    
    return sum

def main():
    selfnum_list = [0] * 10003
    for i in range(1,10001):
        num = self_num(i)
        if num<=10000:
            selfnum_list[num] = 1

    for i in range(1,10001):
        if selfnum_list[i] == 0 :
            print(i)

if __name__ == "__main__":
    main()