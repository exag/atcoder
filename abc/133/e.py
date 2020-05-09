"""dfs
その頂点から見て、この塗り方が何通りあるか？と考える

根以外:
自分と親で2色使っているので、K-2色から、子の数を選ぶ -> K-2 P 子の数
葉の場合は子がいないので、K-2 P 0 = 1 になる（実装上は区別しなくてOK）

根:
根自身の塗り方も考慮する必要があるので、根と子の塗り方を考える
K色から、自分＋子の数を選ぶ -> K P 子の数+1

その都度計算すると間に合わないので、階乗は前計算する
"""
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
INF = float("inf")
MOD = 10 ** 9 + 7


def combination(n, k):
    if k > n - k:
        return combination(n, n - k)
    return fact[n] * ifact[k] * ifact[n - k]


def permitation(n, k):
    # nPk = nCk * k!
    res = combination(n, k) * fact[k]
    return res % MOD


N, K = map(int, input().split())
to = defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

# nまでの階乗を前処理
n = 200005
fact = defaultdict(int)
fact[0] = 1
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i
    fact[i] %= MOD
# nまでの階乗の逆元を前処理
ifact = defaultdict(int)
ifact[n] = pow(fact[n], MOD - 2, MOD)
for i in reversed(range(1, n + 1)):
    ifact[i - 1] = ifact[i] * i
    ifact[i - 1] %= MOD


def dfs(v, p=-1):
    global ans
    for u in to[v]:
        if u == p:
            continue
        dfs(u, v)
    if p == -1:
        nk = K
        c = len(to[v]) + 1
    else:
        nk = K - 2
        c = len(to[v]) - 1
    ans *= permitation(nk, c)
    ans %= MOD


ans = 1
dfs(0)
print(ans)
