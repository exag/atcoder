N, K, M = map(int, input().split())
A = list(map(int, input().split()))

all = M * N
need = all-sum(A)
if need > K:
    print(-1)
    exit()
if need <= 0:
    print(0)
    exit()

print(need)
