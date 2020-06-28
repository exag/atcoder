"""２分探索
順番は関係なく、
結局「Aの前からi個選ぶ、Bの前からj個選ぶ」だけ考えればよい

iを固定して、jをどれだけ大きくできるかを２分探索で探す
"""
from itertools import accumulate
import bisect


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [0] + list(accumulate(A))
B = [0] + list(accumulate(B))

ans = 0
for i in range(N+1):
    a = A[i]
    if a > K:
        break
    r = K - a
    j = bisect.bisect(B, r) - 1
    ans = max(ans, i + j)

print(ans)
