from collections import defaultdict
N, M = map(int, input().split())

subs = defaultdict(list)
for i in range(M):
    p, s = map(str, input().split())
    p = int(p)
    subs[p].append(s)

ac = 0
pena = 0
for k, v in subs.items():
    wa = 0
    for a in v:
        if a == 'AC':
            ac += 1
            pena += wa
            break
        wa += 1

print(ac, pena)
