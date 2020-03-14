N = int(input())
a = list(map(int, input().split()))
ans = 0
tmp = 1
for i in range(1, N):
    if a[i-1] < a[i]:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 1
ans = max(ans, tmp)
print(ans)