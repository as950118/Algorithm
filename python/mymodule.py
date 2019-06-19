def combination(n, m):
    for i in range(1, m):
        n *= (n-i)
        m *= (m-i)
        if n % m == 0:
            n //= m
            m = 1
    return n
