"""
dp[i][sum_v] := i-1 番目までの品物から価値が sum_v 以上を達成するように
選んだときの、重さの総和の最小値

dp[N][sum_v] の値が、W 以下であるような、sum_v の値の最大値が答え
"""
N, W = map(int, input().split())
INF = float('inf')
MAX_V = 100100

dp = [[INF for _ in range(MAX_V+1)] for _ in range(N+1)]
dp[0][0] = 0
weight = []
value = []
for i in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

for i in range(N):
    for sum_v in range(MAX_V + 1):
        # i 番目の品物を選ぶ場合
        if sum_v - value[i] >= 0:
            dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v - value[i]] + weight[i])
        # i 番目の品物を選ばない場合
        dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v])

ans = 0
for sum_v in range(MAX_V + 1):
    if dp[N][sum_v] <= W:
        ans = sum_v

print(ans)
