n = int(input())
arr = list(map(int, input().split()))
arr.sort()
odd = [i for i in arr if i%2]
even = [i for i in arr if not i%2]
len_odd = len(odd)
len_even = len(even)
if len_odd>len_even:
    dif = len_odd - len_even
    print(sum(odd[0:dif-1]))
elif len_odd<len_even:
    dif = len_even - len_odd
    print(sum(even[0:dif-1]))
else:
    print(0)
