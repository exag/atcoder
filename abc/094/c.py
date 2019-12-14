u"""
XをソートしたものをYとすると
Y[N-1]とY[N]のどちらかが中央値となるはず
Y[N-1]より小さい数が取り除かれた場合はY[N]が中央値
Y[N-1]以上の数が取り除かれた場合はY[N−1]が中央値
"""
N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)
CL = Y[N//2-1]
CR = Y[N//2]

for x in X:
    if x < CR:
        print(CR)
    else:
        print(CL)
