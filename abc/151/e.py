"""
Aはソートしておく

maxとminは別々に考えてよい
maxを固定したときに、残りの選び方は何通りあるか
-> 固定した数より小さいものから K-1 個選ぶ
minを固定したときに、残りの選び方は何通りあるか
-> これも同じ

場合の数の計算は毎回やると重たいので、
Nまでの階乗と、Nまでの階乗の逆元を前計算しておく
"""
from collections import defaultdict


def combination(a, b):
    if b > a - b:
        return combination(a, a - b)
    return fact[a] * ifact[b] * ifact[a-b]


N, K = map(int, input().split())
A = sorted(map(int, input().split()))
MOD = 10 ** 9 + 7
# 階乗を前処理
fact = defaultdict(int)
fact[0] = 1
for i in range(1, N+1):
    fact[i] = fact[i-1] * i
    fact[i] %= MOD
# 階乗の逆元を前処理
ifact = defaultdict(int)
ifact[N] = pow(fact[N], MOD-2, MOD)
for i in reversed(range(1, N + 1)):
    ifact[i-1] = ifact[i] * i
    ifact[i-1] %= MOD

mx = 0
mn = 0
for i in range(N):
    mx += A[i] * combination(i, K - 1)
    mn += A[i] * combination(N - i - 1, K - 1)
    mx %= MOD
    mn %= MOD
print((mx - mn) % MOD)