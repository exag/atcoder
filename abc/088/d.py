"""
"""

from collections import deque


H, W = map(int, input().split())
M = []
black_before = 0
for i in range(H):
    s = list(input().strip())
    black_before += s.count('#')
    M.append(s)


def bfs(sx, sy):
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    q = deque()
    q.append((sx, sy))
    dist[sy][sx] = 0

    while q:
        x, y = q.popleft()
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
            dist[newy][newx] = dist[y][x] + 1
    return dist[H-1][W-1]


step = bfs(0, 0)

if step == -1:
    print(-1)
    exit()

black_after = H * W - step - 1
print(black_after - black_before)
