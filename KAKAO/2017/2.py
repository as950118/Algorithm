import sys
sys.setrecursionlimit(10000000)

Num = list(range(0,11))
Bonus = ["S","D","T"]
Bonus_B = [1,2,3]
Option = ["*", "#"]
Option_O = [2, -1]

Arr = []
Str = input()
Score = [0,0,0]

def func(s):
    try:
        float(s)
        return 1
    except:
        return 0

def func_Bonus_Option(s, n):
    for i in range(3):
        if s == str(Bonus[i]):
            Score[n] = Score[n]**(i+1)
        else:
            for j in range(2):
                if s == str(Bonus[i]+Option[j]):
                    Score[n] = Score[n]**(i+1)*Option_O[j]
                    if n!=0 and Option[j]!="#":
                        Score[n-1] = Score[n-1]*Option_O[j]

Len = len(Str)

ret = 0
for i in range(Len):
    if i+1<len(Str) and func(Str[i]) != func(Str[i+1]):
        Arr.append(Str[ret:i+1])
        ret = i+1
    if len(Arr)==5:
        Arr.append(Str[ret:])

for i in range(3):
    Score[i] = int(Arr[i*2])

for i in range(0,3):
    func_Bonus_Option(Arr[i*2+1], i)

print(sum(Score))
