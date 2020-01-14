from collections import deque

H, W = map(int, input().split())
M = []
for i in range(H):
    M.append(list(input().strip()))

ans = 0


def bfs(sx, sy):
    global ans
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    q = deque()
    q.append((sx, sy))
    dist[sy][sx] = 0

    while q:
        v = q.popleft()
        x, y = v[0], v[1]
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            newx, newy = x+dx, y+dy
            if not (0 <= newx < W):
                continue
            if not (0 <= newy < H):
                continue
            if M[newy][newx] == '#':
                continue
            if dist[newy][newx] != -1:
                continue
            q.append((newx, newy))
            d = dist[y][x] + 1
            dist[newy][newx] = dist[y][x] + 1
            ans = max(ans, d)


for y in range(H):
    for x in range(W):
        if M[y][x] == '#':
            continue
        bfs(x, y)

print(ans)

