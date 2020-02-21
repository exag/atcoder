MOD = 10 ** 9 + 7
N = int(input())
S1 = input().strip()
S2 = input().strip()
compress = []
before = 0
for i in range(N):
    if before == 2:
        before = 0
        continue
    if S1[i] == S2[i]:
        compress.append(1)
        before = 1
    else:
        compress.append(2)
        before = 2

if compress[0] == 1:
    ans = 3
else:
    ans = 6
for i in range(1, len(compress)):
    if compress[i - 1] == 1 and compress[i] == 1:
        ans *= 2
    if compress[i - 1] == 1 and compress[i] == 2:
        ans *= 2
    if compress[i - 1] == 2 and compress[i] == 1:
        ans *= 1
    if compress[i - 1] == 2 and compress[i] == 2:
        ans *= 3

print(ans % MOD)
