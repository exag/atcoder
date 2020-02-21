import sys
input = lambda: sys.stdin.readline()[:-1]

from collections import defaultdict

sys.setrecursionlimit(10 ** 7)


def dfs(v, parent, d):
    depth[v] = d
    for to, cost in tree[v]:
        if to == parent:
            continue
        dfs(to, v, d + cost)


depth = defaultdict(int)
tree = defaultdict(list)
n = int(input())
for i in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append((b, c))
    tree[b].append((a, c))

q, k = map(int, input().split())
k -= 1

# k からの距離をすべて求める
dfs(k, -1, 0)
for i in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    # (k - x の距離) + (k - y の距離)
    print(depth[x] + depth[y])
