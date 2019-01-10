arr =[]
val = []
for i in range(int(input())):
    title = input()
    try:
        val[arr.index(title)] += 1
    except:
        arr.append(title)
        val.append(0)
max_arr = []
max_val = max(val)
max_idx = arr[val.index(max_val)]
for i in range(len(arr)):
    
print(arr[val.index(max(val))])
