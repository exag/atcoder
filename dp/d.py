"""
"""
N, W = map(int, input().split())

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
weight = []
value = []
for i in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

for i in range(N):
    for sum_w in range(W+1):
        # i 番目の品物を選ぶ場合
        if sum_w >= weight[i]:
            dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w - weight[i]] + value[i])
        # i 番目の品物を選ばない場合
        dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w])

print(dp[N][W])
