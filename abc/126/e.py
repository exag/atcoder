"""UnionFind
"""
import sys
input = sys.stdin.readline


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size(x) < self.size(y):
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


N, M = map(int, input().split())
uf = UnionFind(N)
for i in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    uf.union(x, y)

s = set()
for i in range(N):
    s.add(uf.find(i))

print(len(s))

