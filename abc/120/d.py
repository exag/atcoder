"""
UnionFind木
"""
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
AB = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AB.append((a, b))
AB.reverse()

# すべて崩落した状態
ans = [N*(N-1)//2]

uf = UnionFind(N)
# 後ろから1本ずつ繋げていく
# ただし最後の1本を繋げるのは不要（初期状態は出力しないから）
for i in range(M-1):
    a, b = AB[i]
    inconvenience = ans[-1]
    if uf.find(a) != uf.find(b):
        # 繋がることで不便さが解消される
        inconvenience -= uf.size(a) * uf.size(b)
        uf.union(a, b)
    ans.append(inconvenience)

# 出力は崩落した順
ans.reverse()
for a in ans:
    print(a)
