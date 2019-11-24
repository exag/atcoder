from numpy import cumsum

N = int(input())
L = list(map(int, input().split()))

all = sum(L)
cum = list(cumsum(L))

ans = float('inf')
for i in range(N-1):
    tmp = abs(cum[i]-(all-cum[i]))
    ans = min(ans, tmp)
print(ans)
