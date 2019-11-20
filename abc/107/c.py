# 方針
# 距離がKの区間を全て調べる
# 合計コスト = 両端の距離 + 0から両端への距離の小さい方（どちらから行くとコストが低いか）

N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 10 ** 9
for i in range(N-K+1):
    # 左端
    l = i
    # 右端
    r = i + K - 1
    # 2点間の距離
    d1 = X[r] - X[l]
    # 0から両端への距離の小さい方
    d2 = min(abs(X[l]), abs(X[r]))
    ans = min(ans, d1 + d2)

print(ans)
