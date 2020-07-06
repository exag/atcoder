from collections import defaultdict

N = int(input())
S = defaultdict(int)
for i in range(N):
    s = input().strip()
    S[s] += 1

for status in ["AC", "WA", "TLE", "RE"]:
    print("{} x {}".format(status, S[status]))
