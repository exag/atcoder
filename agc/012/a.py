N = int(input())
A = sorted(map(int, input().split()))

ans = 0
for i in range(N, N * 3, 2):
    ans += A[i]

print(ans)
