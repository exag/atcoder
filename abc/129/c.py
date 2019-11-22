# DP
N, M = map(int, input().split())
broken = set([int(input()) for _ in range(M)])

MOD = 10**9+7
dp = [0 for i in range(N+2)]
dp[N] = 1

for i in reversed(range(N)):
    if i in broken:
        continue
    dp[i] = dp[i+1] + dp[i+2]
    dp[i] %= MOD

print(dp[0])
