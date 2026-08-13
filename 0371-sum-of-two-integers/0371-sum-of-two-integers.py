class Solution:
    def getSum(self, a: int, b: int) -> int:
        n = 12 # carry + 2**10
        def get_bin(x):
            if x < 0:
                x = format(abs(x), 'b').rjust(n, '0')
                x = list(x)
                for i in reversed([j for j in range(0,len(x))]):
                    if x[i] == '1':
                        x[i] = '0'
                    else:
                        x[i] = '1'
                for i in reversed([j for j in range(1,len(x))]):
                    if x[i] == '1':
                        x[i] = '0'
                    else:
                        x[i] = '1'
                        break
                return ''.join(x)
            return format(x, 'b').zfill(n)
        bin_a = list(get_bin(a))
        bin_b = list(get_bin(b))
        print(get_bin(a), get_bin(b))
        carry = 0
        for i in reversed([j for j in range(0,n)]):
            print(i, ''.join(bin_a), carry)
            if carry:
                carry = 0
                if bin_a[i] == '1':
                    carry = 1
                    bin_a[i] = '0'
                else:
                    bin_a[i] = '1'
            if bin_a[i] == '1':
                if bin_b[i] == '1':
                    carry = 1
                    bin_a[i] = '0'
            elif bin_b[i] == '1':
                    bin_a[i] = '1'
        print(''.join(bin_a))
        if bin_a[0] == '1':
            for i in reversed([j for j in range(0,len(bin_a))]):
                if bin_a[i] == '1':
                    bin_a[i] = '0'
                else:
                    bin_a[i] = '1'
            for i in reversed([j for j in range(1,len(bin_a))]):
                if bin_a[i] == '1':
                    bin_a[i] = '0'
                else:
                    bin_a[i] = '1'
                    break
            return -int(''.join(bin_a[1:]), 2)
        else:
            return int(''.join(bin_a[1:]), 2)