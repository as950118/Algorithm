presucceed = False
def clicksucceed():
    global presucceed
    if presucceed == False:
        presucceed = True
    else:
        presucceed = False
    return presucceed
i=0
n=100
click = [False for i in range(n)]
n_click = 0
while n_click<90:
    i+=1
    for j in range(n):
        if click[j] == False:
            succeed = clicksucceed()
            click[j] = succeed
            if succeed == True:
                n_click+=1
    print(n_click)
print(i)
