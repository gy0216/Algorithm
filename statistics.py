import sys

def main():
    total_sum = 0 
    numCases = int(sys.stdin.readline().rstrip())
    arr_list = [0]*numCases
    for i in range(0,numCases):
        arr_list[i] = int(sys.stdin.readline().rstrip())
        total_sum+=arr_list[i]

    arr_list.sort()

    #산술평균
    average = total_sum/numCases

    if average>=0 :
        if average-int(average) >= 0.5:
            average_result = int(average)+1
        else :
            average_result = int(average)
    else :
        if average-int(average) >= -0.5 :
            average_result = int(average)
        else :
            average_result = int(average)-1

    #중앙값(반복되는 숫자 제거 후 가운데 값)
    middle_result = arr_list[int(numCases/2)]
    repeat_list=[]

    i = 0
    j = 1
    max_re = 0   #가장 높은 빈도
    re_num_count =1   #가장 높은 빈도의 숫자 개수

    while i<numCases : 
        while j<numCases and arr_list[i] == arr_list[j] :
            j+=1
        
        repeat_list.append([arr_list[i], j-i])

        if j-i>max_re :
                max_re = j-i
                re_num_count=1
        elif j-i==max_re:
                re_num_count+=1

        i = j
        j+=1
        
    #최빈값(반복되는 숫자가 있는 경우 count)

    if re_num_count != 1:
        max_re_num = 0
        count=0

        while True :
            if repeat_list[max_re_num][1] == max_re :
                count+=1
                if count == 2 :
                    break
            max_re_num+=1
        
        repeat_result = repeat_list[max_re_num][0]
    else :
        max_re_num = 0
        while True :
             if repeat_list[max_re_num][1] == max_re :
                break
             max_re_num+=1

        repeat_result = repeat_list[max_re_num][0]

    #범위
    range_result = arr_list[numCases-1] - arr_list[0]

    print(average_result)
    print(middle_result)
    print(repeat_result)
    print(range_result)


if __name__ == "__main__":
    main()