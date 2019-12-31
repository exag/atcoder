"""DFS
木の典型問題らしい

各頂点に加算するスコアを記録して、根からDFSで累積和をとる

input = sys.stdin.readline
を入れないとTLEになる
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


N, Q = map(int, input().split())
G = [[] for _ in range(N)]
P = [0 for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    P[p] += x


def dfs(current, parent):
    for child in G[current]:
        if child == parent:
            continue
        P[child] += P[current]
        dfs(child, current)


dfs(0, -1)

print(' '.join([str(p) for p in P]))
