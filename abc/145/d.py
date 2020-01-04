"""(書きかけ)
1 回の移動で x 座標 +y 座標の値は 3 増えます。なので X+Y が 3 の倍数でないとき答えは 0 です。

3 の倍数のとき、(+1,+2) の移動の回数を n、(+2,+1) の移動の回数を m とすると、各座標の値から
n + 2m = X, 2n + m = Y という連立方程式が得られ、n, m が求まります。n < 0 または m < 0 の
とき答えは 0 です。

そうでないとき、計 n + m 回の移動のうち、どの n 回で (+1,+2) の移動をするか決めればよいので、
答えは n+mCn です。

この値は階乗とその逆元を計算することで O(n + m + log mod) で求める事ができます。工夫により
O(min{n, m}) で求めることもできます。


nCk (mod P) の求め方
n!/k!(n-k)!

a/b (mod P) の求め方は

フェルマーの小定理
x^(p-1) ≡ 1 (mod P)
⇔
x^(p-2) ≡ 1/x (mod P)
"""
# 逆元
# a^{-1} mod を計算する
def mod_inv(a, m):
    return pow(a, m-2, m)


X, Y = map(int, input().split())
MOD = 10 ** 9 + 7

if (X + Y) % 3:
    print(0)
    exit()

n = (X + Y) // 3
nx, ny = X - n, Y - n

if nx < 0 or ny < 0:
    print(0)
    exit()

ans = 1
for i in range(nx + 1, nx + ny + 1):
    ans = ans * i % MOD
for i in range(1, ny + 1):
    ans = ans * mod_inv(i, MOD) % MOD

print(ans)

