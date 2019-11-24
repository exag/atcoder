"""方針
個数Kのグループで全体を覆う。
グループ数をGとすると、以下を満たす最小のGが答えとなる。
N <= K + (K-1)(G-1)
変形すると
G >= (N-1)/(K-1)
"""

from math import ceil

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = ceil((N-1)/(K-1))
print(ans)
