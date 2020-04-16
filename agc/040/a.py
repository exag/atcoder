"""
まず全部0を並べておく
"<" の場合、a[i] < a[i+1] になってなければ a[i+1] = a[i] + 1 で更新する
">" の場合、a[i] > a[i+1] になってなければ a[i] = a[i+1] + 1 で更新する
"""

S = input().strip()
N = len(S)
a = [0] * (N + 1)

for i in range(N):
    if S[i] == "<":
        a[i+1] = max(a[i+1], a[i]+1)

for i in reversed(range(N)):
    if S[i] == ">":
        a[i] = max(a[i+1]+1, a[i])

print(sum(a))

