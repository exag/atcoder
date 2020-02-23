"""N進数
"""
N, K = map(int, input().split())

ans = ''
while N:
    d, m = divmod(N, K)
    ans = str(m) + ans
    N //= K

print(len(ans))
