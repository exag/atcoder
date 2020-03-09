A, B, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 10 ** 9
for i in range(M):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    ans = min(ans, a[x] + b[y] - c)

print(min(ans, min(a) + min(b)))

