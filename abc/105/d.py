"""
ある区間(l-r)の合計がMの倍数であるということは
累積和をBとして、B[l]とB[r]がmodMで等しいということ

なので、累積和のmodMのリストを作って、ループを回して、
同じ数が今までに出た個数を足していったものが答え

今までに出た数 組み合わせ数
0 0
1 1
2 3
3 6
4 10
"""
from itertools import accumulate
from collections import defaultdict


N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
S.extend(accumulate(A))
S = [s % M for s in S]

D = defaultdict(int)
ans = 0
for s in S:
    ans += D[s]
    D[s] += 1

print(ans)
