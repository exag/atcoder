"""
何やってるかわからない
後で復習する
https://www.youtube.com/watch?v=q-mrqE2Q7JQ
"""
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


n, k, c = mii()
s = si()


def get_positions():
    res = []
    i = 0
    while i < n and len(res) < k:
        if s[i] == 'o':
            res.append(i)
            i += c+1
        else:
            i += 1
    return res


l = get_positions()
s = s[::-1]
r = get_positions()
for i in range(k):
    r[i] = n-1-r[i]
s = s[::-1]

lastL = [-1] * (n+1)
for i in range(k):
    lastL[l[i]+1] = i
for i in range(n):
    if lastL[i+1] == -1:
        lastL[i+1] = lastL[i]

lastR = [-1] * (n+1)
for i in range(k):
    lastR[r[i]] = i
for i in reversed(range(n)):
    if lastR[i] == -1:
        lastR[i] = lastR[i+1]


for i in range(n):
    if s[i] == 'x':
        continue
    li = lastL[i]
    ri = lastR[i+1]
    cnt = 0
    if li != -1:
        cnt += li + 1
    if ri != -1:
        cnt += ri + 1
    if li != -1 and ri != -1 and r[ri]-l[li] <= c:
        cnt -= 1
    if cnt >= k:
        continue
    print(i+1)