arr = []
num = []
for elem in input(): #error처리를 위해서 배열에 저장한 후 처리
    try: #int(elem) 이 불가능하면 문자
        if int(elem) == 1:
            num.append("")
        else:
            num.append(elem)
    except:
        if elem.islower(): #소문자라면 대문자와 이어서 처리
            arr[len(arr)-1] += elem
        else:
            arr.append(elem)

if len(arr) != len(num): #개수가 안맞을시
    print("error")
else:
    for i in range(len(arr)):
        print(arr[i]+num[i],end="")
