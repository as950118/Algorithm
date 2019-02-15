import sys

sys.setrecursionlimit(10000000)

def func():

    prv = [0]*3
    cur = [0]*3

    prv = arr[:]

    for i in range(1, n):
        arr = (list(map(int, sys.stdin.readline().strip().split(' '))))

        new_score[0] = max(old_score[0], old_score[1]) + block[i][0]
        new_score[1] = max(old_score[0], old_score[1], old_score[2]) + block[i][1]
        new_score[2] = max(old_score[1], old_score[2]) + block[i][2]

        new_score[0] = min(old_score[0], old_score[1]) + block[i][0]
        new_score[1] = min(old_score[0], old_score[1], old_score[2]) + block[i][1]
        new_score[2] = min(old_score[1], old_score[2]) + block[i][2]

    return max_num, min_num


def main():
    n = sys.stdin.readline().strip()
    print(func())

if __name__ == '__main__':
    main()
