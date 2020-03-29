"""
i 日目の選択をする上で、ずっと昔にどういう選択をしていたかの情報は不要で、
前日のことだけわかっていればいい
dp[i+1][j] := i 日目までの活動履歴のうち、
最終日である i 日目には活動 j (0: A, 1: B, 2: C) を選んだ場合の、
得られる幸福度の最大値
"""
N = int(input())
A = []
B = []
C = []
for i in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0][0] = A[0]
dp[0][1] = B[0]
dp[0][2] = C[0]
for i in range(1, N):
    # B->A, C->A の大きい方
    dp[i][0] = max(dp[i-1][1] + A[i], dp[i-1][2] + A[i])
    # A->B, C->B の大きい方
    dp[i][1] = max(dp[i-1][0] + B[i], dp[i-1][2] + B[i])
    # A->C, B->C の大きい方
    dp[i][2] = max(dp[i-1][0] + C[i], dp[i-1][1] + C[i])
print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))