import sys

floor_list = [ [0]*15 for i in [0]*15 ]

for i in range(0,15):
    floor_list[0][i] = i+1
    floor_list[i][0] = 1

for i in range(1,15):
    for j in range(1,15):
        floor_list[i][j] = floor_list[i-1][j] + floor_list[i][j-1]
#         print(floor_list[i][j], " ",end="")
#     print()

# print()
# print()

# for i in range(0,15):
#     for j in range(0,15):
#         print(floor_list[i][j], " ",end="")
#     print()

# print()
# print()
def be_a_president(floor, no):
        return floor_list[floor][no-1]


def main():
    numCases = int(sys.stdin.readline().rstrip())
    for i in range(0,numCases):
        floor = int(sys.stdin.readline().rstrip())
        no = int(sys.stdin.readline().rstrip())
        num_people = be_a_president(floor,no)

        print(num_people)


if __name__ == "__main__":
    main()