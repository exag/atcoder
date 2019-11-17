from collections import defaultdict

N, M = map(int, input().split())
years = [tuple(map(int, input().split())) for _ in range(M)]

d = defaultdict(int)
b = dict()

for p, y in sorted(years, key=lambda x: x[1]):
    d[p] += 1
    b[y] = '{:06d}{:06d}'.format(p, d[p])

for p, y in years:
    print(b[y])
