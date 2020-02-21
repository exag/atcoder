"""
bisect.bisect_left(a:list, x:int) -> aの中でx以下の数の最大値のindex
bisect.bisect_right(a:list, x:int) -> aの中でxより大きい数の最小値のindex

print(bisect.bisect_left([1,2,3,3,3,4,5], 3))
2
print(bisect.bisect_right([1,2,3,3,3,4,5], 3))
5

"""
import bisect
from itertools import accumulate


N, M = map(int, input().split())
A = sorted(map(int, input().split()))

S = [0] + list(accumulate(A))


def calc(x):
    """
    A[i] + A[j] の組み合わせの中からx以上の数を取るときの、
    個数とその総和のペアを返す
    """
    _total = 0
    _num = 0
    # A[i] を固定して考える
    for i in range(N):
        # x <= A[i] + A[j]
        # x - A[i] <= A[j] なので
        # x - A[i] 以上となる最初の index を求める
        j = bisect.bisect_left(A, x - A[i])
        # その行で選べる個数
        _num += N - j
        # 総和の A[j] 分
        _total += S[N] - S[j]
        # 総和の A[i] 分
        _total += A[i] * (N - j)
    return _total, _num


# 2分探索
# M 個以上が取れるような x のうち最小値求める
left = 0
right = 200005
while right - left > 1:
    center = (left + right) // 2
    if calc(center)[1] >= M:
        left = center
    else:
        right = center

total, num = calc(left)
ans = total
# A[i] + A[j] が同じ数の場合は余分に取れることがあるので、Mを超えた分については減算する
# 余っている分は必ず left になる（重複してるのは1番小さい数のはずだから）
ans -= (num - M) * left
print(ans)
