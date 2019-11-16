def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


N = int(input())
L = list(map(int, input().split()))

ans = L[0]
for i in range(1, N):
    ans = gcd(ans, L[i])

print(ans)
