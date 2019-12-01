"""
DFS
"""
# 再帰回数の上限を解除
import sys
sys.setrecursionlimit(10**7)


class Edge:
    def __init__(self, _to, _id):
        self.to = _to
        self.id = _id


def dfs(vertex, parent_color=-1, parent_vertex=-1):
    color = 1
    for g in graph[vertex]:
        u = g.to
        ei = g.id
        if u == parent_vertex:
            continue
        if color == parent_color:
            color += 1
        ans[ei] = color
        color += 1
        dfs(u, ans[ei], vertex)


N = int(input())
graph = [[] for _ in range(N)]
ans = [0 for _ in range(N-1)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(Edge(b, i))
    graph[b].append(Edge(a, i))

dfs(0)

# 最大次数が色数となる
mx = max([len(g) for g in graph])
print(mx)

for i in range(N-1):
    print(ans[i])
