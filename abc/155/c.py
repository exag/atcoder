from collections import defaultdict

N = int(input())
d = defaultdict(int)
for i in range(N):
    s = input().strip()
    d[s] += 1

L = sorted(d.items(), key=lambda x: -x[1])
MX = L[0][1]

L2 = [l[0] for l in L if l[1] == MX]
L2.sort()

for l in L2:
    print(l)
