for T in range(int(input())):
    n = int(input())
    arr = [0]*(n+1)
    arr_s = [0]*(n+1)

    dp = [[0]*(n+1) for i in range(n+1)]
    knuth = [[0]*(n+1) for i in range(n+1)]
    arr = [0] + list(map(int, input().split()))

    for i in range(1, n+1):
        arr_s[i] = arr_s[i-1] + arr[i]
        dp[i-1][i] = 0
        knuth[i-1][i] = i
    for i in range(2, n+1):
        for j in range(n-i+1):
            k = i+j
            dp[j][k] = 10000000000
            for l in range(knuth[j][k-1], knuth[j+1][k] + 1):
                v = dp[j][l] + dp[l][k] + arr_s[k] - arr_s[j]
                if dp[j][k] > v:
                    dp[j][k] = v
                    knuth[j][k] = l
    print(dp[0][n])
