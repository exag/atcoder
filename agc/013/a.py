si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
lmsi = lambda: list(map(str, input().split()))
smii = lambda: sorted(map(int, input().split()))

# ----------

N = ii()
A = lmii()

B = [A[0]]
for i in range(1, N):
    if B[-1] != A[i]:
        B.append(A[i])

if len(B) <= 2:
    print(1)
    exit()

ans = 1
i = 2
while i < len(B):
    if (B[i]-B[i-1]) * (B[i-1]-B[i-2]) < 0:
        ans += 1
        i += 1
    i += 1

print(ans)