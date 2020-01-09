"""DP
"""
N = int(input())
A = list(map(int, input().split()))
INF = float('inf')

dp = [[-INF for _ in range(2)] for _ in range(N+1)]
dp[0][0] = dp[0][1] = sum(A)
# print(dp)
for i in range(N):
    dp[i+1][0] = max(dp[i][0]+A[i], dp[i][0])
    dp[i+1][1] = max(dp[i+1][0], dp[i][1])

    dp[i+1][1] = max(dp[i+1][1], dp[i][0] - (A[i] + A[i+1]) + (-A[i]-A[i+1]))
    if i > 0:
        dp[i+1][1] = max(dp[i+1][1], dp[i][1] - (-A[i] + A[i+1]) + (A[i]-A[i+1]))

print(max(dp[N-1]))

