class Solution:
    def reverse(self, x: int) -> int:
        # 1. 문자열로 처리하는 방법
        str_x = str(x)

        if str_x[0] == "-":
            ret = int(f"-{str_x[1:][::-1]}")
        else:
            ret = int(str_x[::-1])
        if -(2**31) > ret or ret > 2**31 -1:
            return 0
        return ret
        
        # # 2. 숫자로 처리하는 방법
        # i = 10
        # ret = 0
        # while x>0:
        #     cur = x%i
        #     x = x//i
        #     ret += cur
        #     ret *= i
        # return ret//10