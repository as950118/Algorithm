def func_sum(val):
    val = str(val)
    ret = 0
    for i in val:
        ret += int(i)
    return ret
def func_mul(val):
    val = str(val)
    ret = 1
    for i in val:
        ret *= int(i)
    return ret

def solution(pobi, crong):
    answer = 0
    #예외처리
    if ((pobi[0]+1) != pobi[1]) or((crong[0]+1) != crong[1]):
        return -1

    pobi = max(func_sum(pobi[0]), func_sum(pobi[1]), func_mul(pobi[0]), func_mul(pobi[1]))
    crong = max(func_sum(crong[0]), func_sum(crong[1]), func_mul(crong[0]), func_mul(crong[1]))
    if pobi > crong:
        answer = 1
    elif pobi < crong:
        answer = 2
    else:
        answer = 0
    return answer

print(solution([97,98],[197,198]))
