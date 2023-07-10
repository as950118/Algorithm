'''
문제정의
그룹의 점수들을 입력받고
평균을 구한뒤
평균이 넘는 인원의 비율을 구하기
'''
T = int(input())

def average(arr):
    return sum(arr)/len(arr)
def group_average(arr):
    avg = average(arr)
    count = 0
    for e in arr:
        if e > avg:
            count += 1
    return count/len(arr)

for t in range(T):
    arr = list(map(int,input().split()))    
    num = arr[0]
    # 평균구하기
    avg = average(arr[1:])
    # 평균이 넘는 인원의 비율 구하기
    ret = group_average(arr[1:])
    print(f"{ret*100:0.3f}%")







