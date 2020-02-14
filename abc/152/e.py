from fractions import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def mod_inv(a, m):
    return pow(a, m-2, m)


MOD = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))

LCM = 1
for a in A:
    LCM = lcm(LCM, a)
LCM %= MOD

ans = 0
for a in A:
    ans += LCM * mod_inv(a, MOD) % MOD
    ans %= MOD

print(ans)
