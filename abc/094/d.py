"""
nには1番大きいもの
cはn/2に一番近いもの
"""
N = int(input())
A = sorted(map(int, input().split()), reverse=True)

n = A[0]
m = n/2
c = 1e100
for a in A[1:]:
    if abs(m-a) < abs(m-c):
        c = a

print(n, c)
