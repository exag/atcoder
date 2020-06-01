# 素因数分解
def prime_factorize(n):
    from collections import defaultdict
    e = defaultdict(int)
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            e[i] += 1
            n //= i
    if n != 1:
        e[n] += 1
    return e
