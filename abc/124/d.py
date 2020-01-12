from itertools import groupby
from numpy import cumsum


N, K = map(int, input().split())
S = input().strip()

if len(set(S)) == 1:
    print(N)
    exit()

# ランレングス圧縮
G = []
for k, v in groupby(S):
    G.append(len(list(v)))
# 1 0 1 0 1...の配列が欲しいので、
# 先頭、末尾が0ならダミーの要素をそれぞれ追加する
if S[0] == '0':
    G.insert(0, 0)
if S[-1] == '0':
    G.append(0)

cum = [0]
cum.extend(list(cumsum(G)))
cum.append(0)

ans = 0
gc = len(G)
w = min(gc, 3+(K-1)*2)
for i in range(0, gc-w+2, 2):
    ans = max(ans, cum[i+w]-cum[i])
print(ans)
