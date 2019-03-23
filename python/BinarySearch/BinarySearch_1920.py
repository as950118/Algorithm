import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr1 = list(map(int, input().split())) #탐색될 배열
m = int(input())
arr2 = list(map(int ,input().split())) #탐색할 배열

len1 = len(arr1)
arr1.sort() #탐색될 배열값을 정렬해줘야함

def binarysearch(cur, start,end):
    if start>end: #시작지점이 끝지점보다 높다면 없다고 판단하고 종료
        return 0
    mid = (start+end)//2 #중간값
    val = arr1[mid] #탐색될 배열의 중간값에 해당하는 값
    if cur==val: #탐색할 값이 탐색될 값과 같은 경우
        return 1
    if cur<val:
        return binarysearch(cur, start, mid-1) #중간의 중간보다 한칸 내려감
    else:
        return binarysearch(cur, mid+1, end) #중간의 중간보다 한칸 올라감
for i in arr2:
    print(binarysearch(i, 0, len1-1))
