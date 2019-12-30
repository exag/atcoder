"""DP
例えば K=3 のとき
1, 4, 7, ...回目
2, 5, 8, ...回目
3, 6, 9, ...回目
の結果は独立して考えることができる。

mod K によってK個のグループに分けて、各グループでDPする。
ここからはDPコンテストのCとほぼ同じ。

・出した手
・その手での最大リターン
を保持しておく。
"""
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input().strip()


def pon(computer, mine):
    if computer == 'r' and mine == 2: return P
    if computer == 's' and mine == 0: return R
    if computer == 'p' and mine == 1: return S
    return 0


ans = 0
for st in range(K):
    t = T[st::K]

    l = len(t)
    dp = [[0 for _ in range(3)] for _ in range(l+1)]

    for i in range(l):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp[i+1][k] = max(dp[i+1][k], dp[i][j] + pon(t[i], k))
    ans += max(dp[i+1])
print(ans)
