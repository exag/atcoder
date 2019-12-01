from collections import defaultdict
from itertools import combinations

D = defaultdict(list)
N = int(input())
for i in range(N):
    s = input().strip()
    prefix = s[0]
    if prefix in 'MARCH':
        D[prefix].append(s)

# 接頭語の種類が2以下の場合は終了
if len(D.keys()) < 3:
    print(0)
    exit()

# 接頭語の組み合わせを列挙する
C = combinations(list(D.keys()), 3)

ans = 0
for c0, c1, c2 in C:
    ans += len(D[c0]) * len(D[c1]) * len(D[c2])

print(ans)
