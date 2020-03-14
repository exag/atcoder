N = int(input())
a = list(map(int, input().split()))
sm = a[0]
l = 0
r = 0
ans = 0

while True:
    if sm == N:
        ans += 1
        l += 1
        r += 1
        if r == N:
            break
        sm += a[r]
        sm -= a[l-1]
    elif sm < N:
        r += 1
        if r == N:
            break
        sm += a[r]
    elif sm > N:
        l += 1
        if l == N:
            break
        sm -= a[l-1]

print(ans)