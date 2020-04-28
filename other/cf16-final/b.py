N = int(input())

cum = 0
mx = 0
for i in range(N):
    cum += i + 1
    if cum >= N:
        mx = i + 1
        break

for i in reversed(range(1, mx+1)):
    if N - i >= 0:
        print(i)
        N -= i

