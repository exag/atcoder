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

K = ii()

ans = 0


for i in range(1, K+1):
    for j in range(1, K+1):
        g = gcd(i, j)
        for k in range(1, K+1):
            ans += gcd(g, k)

print(ans)