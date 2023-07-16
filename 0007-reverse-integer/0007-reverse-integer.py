class Solution:
    def reverse(self, x: int) -> int:
#         # 1. 문자열로 처리하는 방법
#         str_x = str(x)

#         if str_x[0] == "-":
#             ret = int(f"-{str_x[1:][::-1]}")
#         else:
#             ret = int(str_x[::-1])
        
#         if -(2**31) > ret or ret > 2**31 -1:
#             return 0

#         return ret
        
        # 2. 숫자로 처리하는 방법
        flag = 1 if x>0 else 0 # 음수=0, 양수=1
        if not flag:
            x = -x
        i = 10
        ret = 0
        while x>0:
            cur = x%i
            x = x//i
            ret += cur
            ret *= i

        ret //= i

        if ret > 2**31 -1:
            return 0
        
        if flag:
            return ret
        else:
            return -ret