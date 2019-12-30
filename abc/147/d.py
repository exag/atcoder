"""bit演算
XORをとる操作で各bitは互いに干渉しないため、bitごとに独立に考えることができる。

各bitのXORの総和は0、1がそれぞれ何個出てくるかがわかると以下で求まる。
(0の個数)*(1の個数)*(2^何桁目か)
これを60桁分ループして足し合わせていけばよい。

Python3 だと TLE
PyPy3 だと AC
"""
MOD = 10**9+7
N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(60):
    x = 0
    for a in A:
        if a >> i & 1:
            x += 1
    ans += x * (N-x) * (2**i)
    ans %= MOD

print(ans)
