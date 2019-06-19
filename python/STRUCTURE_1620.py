import sys
n, m = map(int ,sys.stdin.readline().strip().split())
num = [None for i in range(n)] #순서를 기준으로
name = {} #이름을 기준으로
for i in range(n):
    Input = sys.stdin.readline().strip() #input과 sys.stdin.radline 은 속도차이가 상당함
    num[i]= Input
    name[Input] = i
for i in range(m):
    Input = sys.stdin.readline().strip()
    try: #입력이 숫자일 경우
        print(num[int(Input)-1])
    except: #입력이 숫자가 아닐경우
        print(1+name[Input])
