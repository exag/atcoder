N, x = map(int, input().split())
a = sorted(map(int, input().split()))

ans = 0
for i in range(N):
    ans += 1
    x -= a[i]
    if x < 0:
        ans -= 1
        break
if x > 0:
    ans -= 1
print(max(ans, 0))