N = int(input())
X = list(map(int, input().split()))

ans = 10**10
for i in range(1, 101):
    tmp = 0
    for x in X:
        tmp += (i - x) ** 2
    ans = min(ans, tmp)

print(ans)
