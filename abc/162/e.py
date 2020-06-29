"""
「gcd({A}) = i となる数列 {A} がいくつあるか？」という問題を考えます。

d'i = gcd が i の倍数になる個数
    = (K//i)^N (K//i は i の倍数の個数でこれが N 個あるから)

di = gcd がぴったり i になる個数
   = i の倍数だけど i ぴったりじゃないもの
   = d'i - d2i - d3i - ...

降順で最初の方は di = d'i なので、（2i が K を超えるから）
di を大きい方から計算していくと少ない計算量で求めることができる
"""
MOD = 10 ** 9 + 7
N, K = map(int, input().split())
# di, d'i は同じ配列を使い回す
d = [0] * (K + 1)
# d'i を作る
for i in range(1, K + 1):
    d[i] = pow(K // i, N, MOD)
# di を大きい順に作っていく
for i in reversed(range(1, K + 1)):
    for j in range(2 * i, K + 1, i):
        # d'i から  d2i, d3i, ... を引いていく
        # i より大きい di は d'i ではなく di になっている
        d[i] -= d[j]
        d[i] %= MOD
ans = 0
for i in range(1, K + 1):
    ans += d[i] * i
    ans %= MOD
print(ans)

