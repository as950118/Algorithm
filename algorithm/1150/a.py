[n, m, r] = list(map(int, input().split()))
s = list(map(int, input().split()))
b = list(map(int, input().split()))

min_s: int = min(s)
max_b: int = max(b)

r_s = r // min_s
if r < max_b * r_s + (r - min_s * r_s):
    print(max_b * r_s + (r - min_s * r_s))
else:
    print(r)
