"""2次元累積和
"""
N, M, Q = map(int, input().split())

mat = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
sum = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# 列車の位置を2次元配列にマッピング
for i in range(M):
    L, R = map(int, input().split())
    mat[L][R] += 1
# 2次元累積和の構築
for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum[i][j] = mat[i][j]
        sum[i][j] += sum[i - 1][j]
        sum[i][j] += sum[i][j - 1]
        sum[i][j] -= sum[i - 1][j - 1]
# for m in mat:
#     print(m)
# print("---")
# for s in sum:
#     print(s)
# print("---")
# 2次元累積和から範囲に含まれる個数を取り出す
for i in range(Q):
    L, R = map(int, input().split())
    ans = sum[R][R]
    ans -= sum[R][L - 1]
    ans -= sum[L - 1][R]
    ans += sum[L - 1][L - 1]
    print(ans)
