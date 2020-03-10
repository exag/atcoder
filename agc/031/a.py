"""
すべて異なる文字からなる文字列を作るということは、
aの中から1個選ぶ or 選ばない
bの中から1個選ぶ or 選ばない
...
と言い換えることができる

なので、(aの個数+1) * (bの個数+1) * ... * (zの個数+1) - 1
が答え

最後の-1は何も選ばなかったケースを引いている
"""
from string import ascii_lowercase
from collections import defaultdict


N = int(input())
S = input().strip()
MOD = 10 ** 9 + 7


c = defaultdict(int)
for i in range(N):
    c[S[i]] += 1

ans = 1
for x in ascii_lowercase:
    ans *= c[x] + 1
    ans %= MOD
ans -= 1
ans %= MOD
print(ans)
