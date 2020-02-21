from copy import deepcopy
# 多次元配列を作成する
def make_multi_list(initial, degree):
    ans = [initial for _ in range(degree[-1])]
    for d in reversed(degree[:-1]):
        ans = [deepcopy(ans) for _ in range(d)]
    return ans


H, W = map(int, input().split())
C = []
INF = float('inf')
dist = make_multi_list(INF, [10, 10])

for i in range(10):
    C.append(list(map(int, input().split())))

# ワーシャルフロイド
for i in range(10):
    for j in range(10):
        dist[i][j] = C[i][j]
for k in range(10):
    for i in range(10):
        for j in range(10):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

ans = 0
for i in range(H):
    for n in map(int, input().split()):
        if n == -1:
            continue
        ans += dist[n][1]

print(ans)
