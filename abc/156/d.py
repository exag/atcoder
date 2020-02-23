"""
nC0 + nC1 + ... + nCn = 2^N という性質を使う
"""
def mod_inv(a, m):
    return pow(a, m-2, m)


def combination(a, b):
    if b > a - b:
        return combination(a, a - b)
    ans_mul = 1
    ans_div = 1
    for i in range(b):
        ans_mul *= a - i
        ans_div *= i + 1
        ans_mul %= MOD
        ans_div %= MOD
    ans = ans_mul * mod_inv(ans_div, MOD)
    return ans


MOD = 10**9+7
N, K = map(int, input().split())

ans = pow(N, K, MOD) - 1
ans %= MOD
ans *= mod_inv(2, MOD)
print(ans % MOD)