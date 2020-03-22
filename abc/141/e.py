"""DP
pypy3じゃないとTLE

2つの部分文字列の先頭位置2箇所をすべて試す
何文字一致するかは、ループではなくDPを使う

dp[i][j] = iからとjから始めたときに一致する長さ
これを後ろから埋めていく
"""
N = int(input())
S = input().strip()

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in reversed(range(N)):
    for j in reversed(range(i+1, N)):
        if S[i] != S[j]:
            # 先頭が一致していなければ0
            dp[i][j] = 0
        if S[i] == S[j]:
            # 先頭が一致していれば、その後ろの一致文字数+1
            dp[i][j] = dp[i+1][j+1] + 1

ans = 0
for i in range(N):
    for j in range(i+1, N):
        # 部分文字列同士が重なるといけないので、j-iが上限
        now = min([dp[i][j], j-i])
        ans = max(ans, now)

print(ans)
