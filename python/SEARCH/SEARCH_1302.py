arr =[]
val = []
for i in range(int(input())):
    title = input()
    try: #제목이 있을 경우
        val[arr.index(title)] += 1
    except: #제목이 없을 경우
        arr.append(title)
        val.append(1)

max_val = max(val)
max_arr = arr[val.index(max_val)]

for i in range(len(arr)): #팔린 권수 비교
    try: #최대 팔린 권수와 동일한 권수가 있다면
        val[val.index(max_val)] = 0
        if max_arr>arr[val.index(max_val)]:
            max_arr = arr[val.index(max_val)]
    except Exception as e: #없다면 종료
        break
print(max_arr)
