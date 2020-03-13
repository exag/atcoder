"""２分探索
"""
import bisect
from collections import defaultdict


S = list(input().strip())
T = list(input().strip())
L = len(S)

if not set(T) <= set(S):
    print(-1)
    exit()

d = defaultdict(list)
for i, s in enumerate(S):
    d[s].append(i)

idx = -1
ans = 0
for t in T:
    pos = bisect.bisect_right(d[t], idx)
    if pos == len(d[t]):
        ans += L - idx - 1 + d[t][0] + 1
        idx = d[t][0]
    else:
        ans += d[t][pos] - idx
        idx = d[t][pos]

print(ans)
