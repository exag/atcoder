import heapq
from collections import defaultdict, deque
from math import ceil, factorial
from fractions import gcd
import sys
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7

si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
smii = lambda: sorted(map(int, input().split()))

N, M = mii()
edge = defaultdict(list)
memo = defaultdict(int)
done = defaultdict(bool)


def dp(v):
    if done[v]:
        return memo[v]
    ret = 0
    for to in edge[v]:
        ret = max(ret, dp(to) + 1)
    done[v] = True
    memo[v] = ret
    return ret


for i in range(M):
    x, y = mii()
    edge[x].append(y)
ans = 0
for v in range(1, N+1):
    ans = max(ans, dp(v))

print(ans)
