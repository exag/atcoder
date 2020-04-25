si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
lmsi = lambda: list(map(str, input().split()))
smii = lambda: sorted(map(int, input().split()))

# ----------

H, W = mii()
S = []
A = [['.'] * W for _ in range(H)]
for i in range(H):
    s = list(si())
    S.append(s)

for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            color = '#'
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    ny = y + dy
                    nx = x + dx
                    if not (0 <= ny < H):
                        continue
                    if not (0 <= nx < W):
                        continue
                    if S[ny][nx] == '.':
                        color = '.'
                        break
            A[y][x] = color

R = [['.'] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if A[y][x] == "#":
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    ny = y + dy
                    nx = x + dx
                    if not (0 <= ny < H):
                        continue
                    if not (0 <= nx < W):
                        continue
                    R[ny][nx] = "#"

if R != S:
    print('impossible')
    exit()

print('iossible')
for a in A:
    print(''.join(a))