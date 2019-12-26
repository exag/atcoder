"""
"""
N, W = map(int, input().split())

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
# 1個目の品物の添字が1となるように調整
weight = [0]
value = [0]
for i in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

for i in range(N):
    i += 1
    for sum_w in range(W+1):
        # i 番目の品物を選ぶ場合
        if sum_w >= weight[i]:
            dp[i][sum_w] = max(dp[i][sum_w], dp[i-1][sum_w - weight[i]] + value[i])
        # i 番目の品物を選ばない場合
        dp[i][sum_w] = max(dp[i][sum_w], dp[i-1][sum_w])

print(dp[N][W])
