#최소 자음 2개, 모음 1개
vowel = ['a','e','i','o','u'] #모음 종류
l, c = map(int, input().split())

#자음 모음 구분
arr_consonant = []
arr_vowel = []
for alp in list(map(str, input().split())):
    if alp in vowel:
        arr_vowel.append(alp)
    else:
        arr_consonant.append(alp)

#자음 모음을 각각 개수에 따라 나누기
div_consonant = [[] for i in range(l+1)]
div_vowel = [[] for i in range(l+1)]
def get_combination(arr, n, m, cur, ret_arr): #자음혹은모음, 구하려는 개수, 현재 개수, 시작 위치, 결과문자열
    if m==n: #구하려는 개수와 현재 개수가 같다면 종료
        return ret_arr #결과 문자열을 반환
    ret = ""
    for i in range(cur, len(arr)): #시작 위치부터 자음혹은모음의 크기까지
        ret += get_combination(arr, n, m+1, i+1, ret_arr+arr[i])
    return ret

#개수만큼 쪼개서 저장하기
for i in range(2, l):
    temp = get_combination(arr_consonant, i, 0, 0,"")
    div_consonant[i] = [temp[j:j+i] for j in range(0, len(temp), i)] #i번째배열에 i개씩 쪼개서 저장
for i in range(1, l-1):
    temp = get_combination(arr_vowel, i, 0, 0,"")
    div_vowel[i] = [temp[j:j+i] for j in range(0, len(temp), i)] #i번째배열에 i개씩 쪼개서 저장

ret_arr = [] #결과문자열들을 저장할 배열
for c in range(1,l+1): #1부터 l까지
    for con in div_consonant[c]: #i개의 자음을 꺼내고
        for vow in div_vowel[l-c]: #l-i개의 모음을 꺼내서
            temp = con + vow #합침
            temp_sort = '' #알파벳 순으로 정렬한 값을 저장하기 위해
            for i in sorted(temp): #알파벳 순으로 정렬하여
                temp_sort += i #저장
            ret_arr.append(temp_sort) #결과문자열들을 저장할 배열에 저장

ret_arr.sort() #결과문자열들을 저장한 배열을 알파벳 순으로 정렬
for ret in ret_arr: #출력
    print(ret)
