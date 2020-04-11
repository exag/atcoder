import heapq
from collections import defaultdict, deque
from math import ceil, factorial
from fractions import gcd
import sys

sys.setrecursionlimit(10 ** 7)
INF = float("inf")
MOD = 10 ** 9 + 7

si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
smii = lambda: sorted(map(int, input().split()))


def func(a, b, c):
    if a % 2 or b % 2 or c % 2:
        return 0
    if a == b == c:
        return -1
    return func((b + c) // 2, (a + c) // 2, (b + c) // 2) + 1


A, B, C = mii()

print(func(A, B, C))
