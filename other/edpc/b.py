"""
Python3 だと TLE
PyPy3 だと AC
"""
INF = float("inf")
N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [INF for i in range(N + K)]
dp[0] = 0
for i in range(N):
    for j in range(1, K + 1):
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))

print(dp[N - 1])
