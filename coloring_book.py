import sys
import math

arr = [[0,-1],[0,1],[-1,0],[1,0]]
result = []
m= 3
n= 3
picture = [[1,0,1],[0,1,0],[1,0,1]]
Matrix = [[0] * n for i in range(m)]

def pic_count(i,j,value):
    for p in range(4):
        col = i+arr[p][0]
        row = j+ arr[p][1]
        if col < 0 or row <0 or col >= m or row >= n:
            continue
        elif picture[col][row] == value and Matrix[col][row] == 0 :
            Matrix[col][row] =1
            result[len(result)-1] +=1
            pic_count(col, row , value)


def main():

    for i in range(m):
        for j in range(n):
            if Matrix[i][j] == 0 and picture[i][j] != 0 :
                result.append(1)
                Matrix[i][j] = 1
                pic_count(i,j,picture[i][j])

    # print(result)
    print(len(result), max(result))




if __name__ == "__main__":
    main()