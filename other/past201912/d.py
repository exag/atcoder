from collections import defaultdict


N = int(input())
A = [int(input()) for _ in range(N)]
D = defaultdict(int)
for i in range(N):
    D[A[i]] += 1
before = 0
after = 0
for i in range(N):
    n = i + 1
    if D[n] == 0:
        before = n
    if D[n] == 2:
        after = n
if after:
    print(after, before)
else:
    print('Correct')