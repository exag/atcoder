"""
* * * * * 辺数 0 -> 連結成分数 5
*-* * * * 辺数 1 -> 連結成分数 4
*-* * *-* 辺数 2 -> 連結成分数 3
*-*-* *-* 辺数 3 -> 連結成分数 2
*-*-*-*-* 辺数 4 -> 連結成分数 1

というように、辺が 1 増えるごとに連結成分は 1 減っていく

つまり、
連結成分の個数 = 頂点数 - 辺数
と言い換えることができる

L, R の組み合わせに対しては、
Σ連結成分の個数 = Σ(頂点数 - 辺数)
Σ連結成分の個数 = Σ(頂点数) - Σ(辺数)
となる

Σ(頂点数), Σ(辺数) についてはそれぞれ独立に考えられる

V = Σ(頂点数) の数え方
https://www.youtube.com/watch?v=IMwigbYzLbI&feature=youtu.be&t=7055

V = Σ(辺数) の数え方
https://www.youtube.com/watch?v=IMwigbYzLbI&feature=youtu.be&t=7235
"""
N = int(input())
V = 0
E = 0
for i in range(N+1):
    V += i * (N-i+1)
for i in range(N-1):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    E += a * (N-b+1)
ans = V - E
print(ans)
