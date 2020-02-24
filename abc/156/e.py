"""
TODO: 後で書く
"""
from collections import defaultdict


def combination(a, b):
    if b > a - b:
        return combination(a, a - b)
    return fact[a] * ifact[b] * ifact[a-b]


MOD = 10**9+7
n, k = map(int, input().split())
k = min(k, n-1)
# 階乗を前処理
fact = defaultdict(int)
fact[0] = 1
for i in range(1, n+1):
    fact[i] = fact[i-1] * i
    fact[i] %= MOD
# 階乗の逆元を前処理
ifact = defaultdict(int)
ifact[n] = pow(fact[n], MOD-2, MOD)
for i in reversed(range(1, n + 1)):
    ifact[i-1] = ifact[i] * i
    ifact[i-1] %= MOD

ans = 0
for i in range(k+1):
    ans += combination(n, i) * combination((n-i-1)+i, i)
    ans %= MOD

print(ans % MOD)
