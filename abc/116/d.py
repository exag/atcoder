"""
解説放送の解放で解く
https://www.youtube.com/watch?v=U3wtVmwxVoI

各数字で
A: 最初に出てくるときの点数（list1）
B: 2回目以降の点数（list0）
にグループ分けし、それぞれ降順にソートする

A から大きい順に選んで、足りなければ B から大きい順に選んだもの
（つまり種類を最大化したもの）を初期セットとする

セット中の最小値 > B の最大値なら、入れ替えてみる
（これ以外だと種類が無駄に減るだけなのでスコアが増えることはない）

入れ替えてみてスコアが増えるなら同じ操作を繰り返していく
増えないなら、次も増えないので、繰り返しを終了する
"""
N, K = map(int, input().split())

td = []
for i in range(N):
    t, d = map(int, input().split())
    td.append((t, d))
td.sort(key=lambda x: (x[0], -x[1]))

list0 = []
list1 = []
set1 = set()
for t, d in td:
    if t not in set1:
        set1.add(t)
        list1.append(d)
    else:
        list0.append(d)
list0.sort(reverse=True)
list1.sort(reverse=True)

select0 = []
select1 = []
variety = min(K, len(list1))
for i in range(variety):
    # 選んものは元のリストから削除する（その方が後で都合がいいから）
    select1.append(list1.pop(0))
if K > variety:
    for i in range(K - variety):
        select0.append(list0.pop(0))

# 配列のsumを毎回取るとTLEするので変数にして加減していく
sum0 = sum(select0)
sum1 = sum(select1)
ans = sum0 + sum1 + variety ** 2
while list0 and list0[0] > select1[-1]:
    # 先に入れ替えてみて、スコアが増えないならbreakで抜ける
    sum0 += list0.pop(0)
    sum1 -= select1.pop(-1)
    variety -= 1
    tmp = sum0 + sum1 + variety ** 2
    if tmp <= ans:
        break
    ans = tmp

print(ans)
