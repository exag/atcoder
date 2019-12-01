u"""
DP
"""

INF = float('inf')
N = int(input())

dp = [INF for _ in range(N+1)]
dp[0] = 0

for i in range(1, N+1):
    # 1円玉を使う場合の枚数で更新
    dp[i] = min(dp[i], dp[i-1] + 1)
    # 6べき円玉を使う場合の枚数で更新
    power = 6
    while i-power >= 0:
        dp[i] = min(dp[i], dp[i-power] + 1)
        power *= 6
    # 9べき円玉を使う場合の枚数で更新
    power = 9
    while i-power >= 0:
        dp[i] = min(dp[i], dp[i-power] + 1)
        power *= 9

print(dp[N])
