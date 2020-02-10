from itertools import accumulate


N, K = map(int, input().split())
P = list(map(int, input().split()))

d = {}
for i in range(1, 1001):
    d[i] = (i + 1) * (i / 2) / i

E = []
for p in P:
    E.append((p+1)/2)

cum = list(accumulate(E))
mx = 0
idx = 0
ans = 0
for i in range(N-K+1):
    if i == 0:
        mx = max(mx, cum[i+K-1])
    else:
        mx = max(mx, cum[i+K-1] - cum[i-1])

print(mx)
