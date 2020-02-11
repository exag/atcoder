"""
Python3 だと TLE
PyPy3 だと AC
"""
INF = float('inf')
N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [INF for _ in range(N)]
dp[0] = 0
for i in range(N):
    for j in range(K):
        j += 1
        if i + j < N:
            dp[i+j] = min(dp[i+j], dp[i] + abs(h[i+j] - h[i]))

print(dp[N-1])
