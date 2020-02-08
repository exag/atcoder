"""解法1
コンビネーションを自前で実装
"""
# 逆元
# a^{-1} mod を計算する
def mod_inv(a, m):
    return pow(a, m-2, m)


def combination(a, b):
    if b > a - b:
        return combination(a, a - b)

    # 10C3 = (10*9*8)/(3*2*1)
    # 10*9*8 -> ans_mul
    # 3*2*1 -> ans_div
    ans_mul = 1
    ans_div = 1
    for i in range(b):
        ans_mul *= a - i
        ans_div *= i + 1
        ans_mul %= MOD
        ans_div %= MOD
    # ans_mul / ans_div をやりたい
    # ans_div の逆元を使って求める
    ans = ans_mul * mod_inv(ans_div, MOD)
    return ans


N, M = map(int, input().split())
MOD = 10**9+7
# M を素因数分解
rest = M
ans = 1
for i in range(2, int(M ** 0.5) + 1):
    cnt = 0
    while rest % i == 0:
        cnt += 1
        rest //= i
    # cnt が 2^X 1とか 3^X の X の部分
    ans *= combination(N+cnt-1, N-1)
    ans %= MOD
# 最後に素数が残ってる文を処理する
if rest != 1:
    cnt = 1
    ans *= combination(N+cnt-1, N-1)
    ans %= MOD

print(ans)
