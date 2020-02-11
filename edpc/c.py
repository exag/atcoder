"""
i 日目の選択をする上で、ずっと昔にどういう選択をしていたかの情報は不要で、
前日のことだけわかっていればいい
dp[i+1][j] := i 日目までの活動履歴のうち、
最終日である i 日目には活動 j (0: A, 1: B, 2: C) を選んだ場合の、
得られる幸福度の最大値
"""
INF = float('inf')
N = int(input())
H = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(N+1)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i+1][k] = max(dp[i+1][k], dp[i][j] + H[i][k])

ans = 0
for i in range(3):
    ans = max(ans, dp[N][i])

print(ans)
