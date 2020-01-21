"""桁DP
http://drken1215.hatenablog.com/entry/2019/02/04/013700

まず各桁は独立に考えて良い
各桁に1が何個あるのかをすべてのAについて集計すると、
Xに0を選んだ時/1を選んだ時のスコアを出が出せる

DPでXを先頭から1桁ずつを決めていくが、その時の遷移は、
これまでえらんだ桁が
1. K未満 -> K未満
2. Kぴったり -> K未満
3. Kぴったり -> Kぴったり
の３通りしかない
K未満 -> Kぴったり の遷移はありえない
ex)
K=5(0b101)で2桁目から3桁目への遷移
1. 01 -> 011
2. 10 -> 100
3. 10 -> 101

後で書く

"""
MAX_DIGIT = 50
SMALL = 1
EQUAL = 0

N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-1 for _ in range(2)] for _ in range(100)]
dp[0][0] = 0

for d in range(MAX_DIGIT):
    mask = 1 << (MAX_DIGIT - d - 1)
    # A で元々 d 桁目にビットが立っているものの個数
    num = 0
    for i in range(N):
        if A[i] & mask:
            num += 1

    # X の d 桁目を 0, 1 にしたときのスコア
    cost0 = mask * num  # 元々の 1 の個数
    cost1 = mask * (N - num)  # 元々の 0 の個数(反転するから)

    # "K 未満 -> K 未満" の遷移
    if dp[d][SMALL] != -1:
        # 0 でも 1 でも自在に大きい方
        dp[d+1][SMALL] = max(dp[d+1][SMALL], dp[d][SMALL] + max(cost0, cost1))

    # "K ぴったり -> K 未満" の遷移
    if dp[d][EQUAL] != -1:
        if K & mask:
            # K の d 桁目が 1 だったら、X の d 桁目は 0 にする
            dp[d+1][SMALL] = max(dp[d+1][SMALL], dp[d][EQUAL] + cost0)

    # "K ぴったり -> K ぴったり" の遷移
    if dp[d][EQUAL] != -1:
        if K & mask:
            dp[d+1][EQUAL] = max(dp[d+1][EQUAL], dp[d][EQUAL] + cost1)
        else:
            dp[d+1][EQUAL] = max(dp[d+1][EQUAL], dp[d][EQUAL] + cost0)


ans = max(dp[MAX_DIGIT][EQUAL], dp[MAX_DIGIT][SMALL])
print(ans)
