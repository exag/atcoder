from collections import defaultdict

N = int(input())
V = list(map(int, input().split()))

# コーナーケースは先に終わらせる
# 全部同じ数の場合は、N/2が答え
if len(set(V)) == 1:
    print(N//2)
    exit()
# 2つしかない場合は1が答え
if N == 2:
    print(1)
    exit()

# 方針: 偶数番目と奇数番目は分けて考える
# 偶数番目、奇数番目はそれぞれの最頻値に合わせるのが低コスト
# 最頻値が同じ場合は「数列に現れる数はちょうど2種類」の制約を外れるので、2番目に多い数にあわせる
d_even = defaultdict(int)
d_odd = defaultdict(int)

for i in range(N):
    v = V[i]
    if i % 2 == 0:
        d_even[v] += 1
    else:
        d_odd[v] += 1

l_even = sorted(d_even.items(), key=lambda x: -x[1])
l_odd = sorted(d_odd.items(), key=lambda x: -x[1])

if l_even[0][0] != l_odd[0][0]:
    print(N - l_even[0][1] - l_odd[0][1])
else:
    # どちらも試してコストの小さい方を採用する
    ans1 = N - l_even[0][1] - l_odd[1][1]
    ans2 = N - l_even[1][1] - l_odd[0][1]
    print(min(ans1, ans2))
