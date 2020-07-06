"""bit全探索
"""
H, W, K = map(int, input().split())
C = []
for i in range(H):
    c = list(input().strip())
    C.append(c)

ans = 0
for h in range(1 << H):
    for w in range(1 << W):
        cnt = 0
        for i in range(H):
            for j in range(W):
                if h >> i & 1:
                    # bitが立っている行は飛ばす
                    continue
                if w >> j & 1:
                    # bitが立っている列は飛ばす
                    continue
                if C[i][j] == "#":
                    # 黒をカウント
                    cnt += 1
        if cnt == K:
            ans += 1

print(ans)
