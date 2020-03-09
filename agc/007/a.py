H, W = map(int, input().split())
bl = 0
br = 0
for i in range(H):
    line = input().strip()
    foot = []
    for j in range(W):
        if line[j] == '#':
            foot.append(j)
    nl = foot[0]
    nr = foot[-1]
    if nl < br:
        print('Impossible')
        exit()
    bl, br = nl, nr
print('Possible')
