N = int(input())
d = [[0 for _ in range(10)] for _ in range(10)]

for i in range(1, N+1):
    S = str(i)
    s = int(S[0])
    t = int(S[-1])
    d[s][t] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += d[i][j] * d[j][i]

print(ans)
