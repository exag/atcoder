import heapq
from collections import defaultdict, deque
from math import ceil, factorial, gcd
import sys
import bisect


sys.setrecursionlimit(10 ** 7)
INF = float("inf")
MOD = 10 ** 9 + 7

si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
smii = lambda: sorted(map(int, input().split()))


N = ii()
S = si()

r_cnt = S.count('R')
g_cnt = S.count('G')
b_cnt = S.count('B')

ans = r_cnt * g_cnt * b_cnt

for i in range(N):
    for dist in range(N):
        j = i + dist
        k = j + dist
        if k >= N:
            break
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            ans -= 1

print(ans)