"""DP
最後に食べる料理が何かだけが重要で、それまでの順番はどうでもいい
そして、Tまでに食べ始めていればいいので、一番時間がかかる料理を最後に持ってきた方が得
-> Aの照準にソートする

dp[i][j] = i個目までの中からAの和がj以下になるように食べたときのBの和のmax
と設定して、k番目を最後の料理とすると、

dp[k-1][T-1] + B[k]
が最後にkを食べたときの最大値

これをすべてのkについて求めて、それらの最大値が答え
"""
N, T = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
AB.sort()

ans = 0
dp = [[0 for _ in range(3005)] for _ in range(3005)]
for i in range(N):
    a, b = AB[i]
    for j in range(T):
        # iを食べるパターン
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        # iを食べないパターン
        nj = j + a
        if nj < T:
            dp[i + 1][nj] = max(dp[i + 1][nj], dp[i][j] + b)
    now = dp[i][T - 1] + b
    ans = max(ans, now)

print(ans)
