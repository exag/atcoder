"""
x 個の隣り合わせの組ができるとすると
グループ数: N - x (x が 1 つ増えるごとにグループは1つ減る)

A. グループの色の割当: M * (M - 1) ^ (N - x - 1)
1 つ目は M 色どれを選んでも良いので M、
2 つ目からは直前にに選んだ色以外なので M - 1
グループ数 - 1 つ目 -> (N - x - 1) 個

B. グループの分け方: N-1 C x

A * B が x を固定したときの組み合わせ
すべての x の場合の総和が答え
"""
from collections import defaultdict

MOD = 998244353

def combination(a, b):
    if b > a - b:
        return combination(a, a - b)
    return fact[a] * ifact[b] * ifact[a-b]


N, M, K = map(int, input().split())

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

ans = 0
# 色の割当 M*(M-1)^(N-x-1) は x が1つ減るごとに、*(M-1) されていくので
# 逆順にループして、1つ前の値に乗算していく
# (その都度計算すると、python では TLE する)
color = M
for x in reversed(range(N)):
    now = combination(N-1, x)
    now *= color
    now %= MOD
    color *= M - 1
    color %= MOD
    # x > K の時も color の計算に必要
    if x <= K:
        ans += now
        ans %= MOD

print(ans)
