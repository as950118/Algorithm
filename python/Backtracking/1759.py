#최소 자음 2개, 모음 1개
vowel = ['a','e','i','o','u'] #모음 종류
l, c = map(int, input().split())
arr = list(map(str, input().split()))
arr_vowel = []
arr_consonant = []
for alp in arr:
    if alp in vowel:

print(arr)
