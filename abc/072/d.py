"""
左から貪欲に入れ替えていく
最後に右端をチェックして必要なら入れ替える
"""
N = int(input())
P = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    if i+1 == P[i]:
        P[i], P[i+1] = P[i+1], P[i]
        ans += 1
if N == P[N-1]:
    ans += 1

print(ans)
