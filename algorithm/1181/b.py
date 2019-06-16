l = int(input())
n = str(input())
ret = int(n)
mod_l = l//2
if l%2:
    for i in range(mod_l):
        if int(n[mod_l+i+1]):
            temp = int(n[:mod_l+i+1]) + int(n[mod_l+i+1:])
        else:
            temp = ret
        if int(n[mod_l-i]):
            temp = min(temp, int(n[:mod_l-i]) + int(n[mod_l-i:]))
        if ret>temp:
            ret = temp
            break
else:
    for i in range(mod_l):
        if int(n[mod_l+i]):
            temp = int(n[:mod_l+i]) + int(n[mod_l+i:])
        else:
            temp = ret
        if int(n[mod_l-i]):
            temp = min(temp, int(n[:mod_l-i]) + int(n[mod_l-i:]))
        if ret>temp:
            ret = temp
            break
print(ret)