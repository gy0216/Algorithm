import sys
import math

arr = [[0,1],[1,0]]
count = [0]
m= 3
n= 6
city_map = [[0, 2, 0, 0, 0, 2], [0, 0, 2, 0, 1, 0],
[1, 0, 0, 2, 2, 0]]

def road(i,j,bi,bj):
    if i == m-1 and j == n-1 :
        count[0] +=1
        # print(count)
    else :
        for p in range(2):
            col = i + arr[p][0] 
            row = j + arr[p][1]
            if col <0 or row <0 or col >= m or row >= n :
                continue
            elif city_map[i][j] == 0:
                road(col,row,i,j)
            elif city_map[i][j] == 1:
                continue
            elif city_map[i][j] ==2:
                c = i - bi

                if c==1 :
                    if col - i == 1:
                        road(col,row,i,j)
                elif c != 1:
                    if col - i != 1:
                        road(col,row,i,j)

def main():

    road(0,0,0,0)

    print(count[0] % 20170805)

if __name__ == "__main__":
    main()