"""
https://www.youtube.com/watch?v=nCHz87GMdpo
http://ronly.hatenablog.com/entry/2017/10/14/162524
a + b < c となる場合が存在すれば -1
a + b = cとなる辺cは必要なし
a + b > cとなる辺cは必要あり
"""
import copy

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
B = copy.deepcopy(A)
for i in range(N):
    for j in range(i, N):
        for k in range(N):
            if not (i != j and j != k and k != i):
                continue
            # a + b < c となる場合が存在すれば -1
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                exit()
            # a + b = cとなる辺cは必要なし
            if A[i][j] == A[i][k] + A[k][j]:
                B[i][j] = 0
# 残った辺の和を取れば良い
ans = 0
for i in range(N):
    for j in range(i, N):
        ans += B[i][j]

print(ans)

