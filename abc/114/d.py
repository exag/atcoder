u"""
解説PDF通り
https://img.atcoder.jp/abc114/editorial.pdf

一般に、ある数 N を
N = P1^e1 * P2^e2 * ... * Pk^ek
と表すとき、約数の数 D は
D = (e1+1)*(e2+1)*...*(ek+1)
となる


"""
## 別解
# N = int(input())
#
# # 1〜N をそれぞれ素因数分解して合算することで N! を素因数分解する
# e = [0] * (N+1)
# for i in range(2, N+1):
#     cur = i
#     for j in range(2, i+1):
#         while cur % j == 0:
#             e[j] += 1
#             cur //= j

from math import factorial

N = int(input())

# N! を素因数分解
fact = factorial(N)
e = [0] * (N+1)
for i in range(2, N+1):
    while fact % i == 0:
        e[i] += 1
        fact //= i


def num(m):
    return len(list(filter(lambda x: x >= m-1, e)))


ans = 0
ans += num(75)
ans += num(25) * (num(3) - 1)   # -1 するのは、num(25) には num(3) が含まれているので、重複を除くため
ans += num(15) * (num(5) - 1)
ans += num(5) * (num(5) - 1) * (num(3) - 2) // 2

print(ans)
