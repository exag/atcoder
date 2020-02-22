class UnionFind:
    def __init__(self, n):
        self.n = n
        # 各要素の親要素の番号を格納するリスト
        # 要素が根（ルート）の場合は-(そのグループの要素数)を格納する
        self.parents = [-1] * n

    def find(self, x):
        """要素xが属するグループの根を返す
        """
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        """要素xが属するグループと要素yが属するグループをくっつける
        """
        x = self.find(x)
        y = self.find(y)
        # すでにくっつてるのでそのまま返す
        if x == y:
            return
        # 大きい方(x)に小さい方(y)をくっつけたいので、
        # 大小が逆なら入れ替える
        if self.size(x) < self.size(y):
            x, y = y, x
        # xのサイズを更新する
        self.parents[x] += self.parents[y]
        # yの親をxに変更する
        self.parents[y] = x

    def size(self, x):
        """要素xが属するグループのサイズ（要素数）を返す
        """
        return -self.parents[self.find(x)]


N, M = map(int, input().split())
P = list(map(int, input().split()))

uf = UnionFind(N+1)

for _ in range(M):
    x, y = map(int, input().split())
    uf.union(x, y)

ans = 0
for i in range(N):
    if uf.find(i+1) == uf.find(P[i]):
        ans += 1

print(ans)

