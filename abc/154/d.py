"""累積和
"""
from itertools import accumulate


N, K = map(int, input().split())
P = list(map(int, input().split()))
E = [(p+1)/2 for p in P]

cum = [0]
cum.extend(list(accumulate(E)))

ans = 0
for i in range(N-K+1):
    ans = max(ans, cum[i+K] - cum[i])

print(ans)
