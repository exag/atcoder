"""
素因数分解して、型の数を 1, 2, 3, ... と超えるまで足していく
2^8 なら
1+2+3=6で3つ
1+2+3+4=10なので4つはダメ
"""
from collections import defaultdict

N = int(input())

if N == 1:
    print(0)
    exit()

e = defaultdict(int)
for i in range(2, int(N ** 0.5) + 1):
    while N % i == 0:
        e[i] += 1
        N //= i
if N != 1:
    e[N] += 1


if len(e) == 0:
    print(1)
    exit()

ans = 0
for k, v in e.items():
    tmp = 0
    i = 0
    while tmp + i + 1 <= v:
        i += 1
        tmp += i
    ans += i

print(ans)