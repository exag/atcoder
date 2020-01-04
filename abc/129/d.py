"""
連続で何マス照らせるかを、縦横それぞれで記録しておく。
縦の数 + 横の数 -1(重複分) が答え
"""
H, W = map(int, input().split())
M = [list(input().strip()) for _ in range(H)]
M_yoko = [[0 for _ in range(W)] for _ in range(H)]
M_tate = [[0 for _ in range(W)] for _ in range(H)]

for row in range(H):
    walls = [-1]
    for col in range(W):
        if M[row][col] == '#':
            walls.append(col)
    walls.append(W)
    for i in range(len(walls)-1):
        st = walls[i]
        ed = walls[i+1]
        for j in range(st+1, ed):
            M_yoko[row][j] = ed - st - 1

for col in range(W):
    walls = [-1]
    for row in range(H):
        if M[row][col] == '#':
            walls.append(row)
    walls.append(H)
    for i in range(len(walls)-1):
        st = walls[i]
        ed = walls[i+1]
        for j in range(st+1, ed):
            M_tate[j][col] = ed - st - 1

ans = 0
for row in range(H):
    for col in range(W):
        ans = max(ans, M_yoko[row][col] + M_tate[row][col] - 1)

print(ans)
