"""DFS解法
"""
import sys
from collections import defaultdict


sys.setrecursionlimit(10**7)

buka = defaultdict(list)
N = int(input())
for i in range(1, N):
    b = int(input())
    b -= 1
    buka[b].append(i)


def dfs(p):
    if not buka[p]:
        return 1

    mx = 0
    mn = 1001001001
    for v in buka[p]:
        s = dfs(v)
        mx = max(mx, s)
        mn = min(mn, s)
    return mn + mx + 1


print(dfs(0))
