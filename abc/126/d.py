"""BFS
https://www.youtube.com/watch?v=26AWkQNRb-A

以下、与えられたグラフを適当な頂点を根とみなした根付き木として考えます。
また根から頂点 i への距離を di とします。

任意の 2 頂点 u と v について、その最小共通祖先を w とすると、
u と v の距離は du + dv − 2dw と書くことができます。

この式の第 3 項は偶数なので、du と dw の偶奇が等しいときに限り、u と w の距離は偶数になります。

よって例えば di が偶数の頂点は白に、奇数の頂点は黒に塗ることで条件を満たす塗り分けが可能です。
"""
from collections import deque

N = int(input())
G = [[] for _ in range(N)]  # (頂点, コスト)
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))

ans = [-1 for _ in range(N)]
q = deque()

# 0 を頂点とする
ans[0] = 0
q.append(0)

while q:
    v = q.popleft()
    for u, w in G[v]:
        if ans[u] != -1:
            continue
        ans[u] = (ans[v] + w) % 2
        q.append(u)

for a in ans:
    print(a)
