"""DFS
https://www.youtube.com/watch?v=F2p_e6iKxnk&feature=youtu.be
「高橋君が青木君より先に到達することができるような葉のうち、青木君から最も遠いもの」を目指すのが最善行動
そして、その葉の一つ手前で捕まる
"""
import sys
sys.setrecursionlimit(10**7)


N, u, v = map(int, input().split())
u -= 1
v -= 1

# 隣接リストに木の状態を持つ
graph = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


dist = []
def dfs(v, depth=0, parent=-1):
    global dist
    dist[v] = depth
    for u in graph[v]:
        # 親には行かないようにする
        if u == parent:
            continue
        dfs(u, depth + 1, v)


def calc_dist(s):
    global dist
    dist = [0 for _ in range(N)]
    dfs(s)
    return dist


# 高橋君の初期位置からの距離
dist_u = calc_dist(u)
# 青木君の初期位置からの距離
dist_v = calc_dist(v)

mx = 0
for i in range(N):
    if dist_u[i] < dist_v[i]:
        # 高橋君が先にいける葉のうち、青木君からの遠いものを更新
        mx = max(mx, dist_v[i])

# 一つ手前で捕まるので−1
print(mx - 1)
