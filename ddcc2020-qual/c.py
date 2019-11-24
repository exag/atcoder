from numpy import cumsum

H, W, K = map(int, input().split())

field = []
for h in range(H):
    field.append(list(input().strip()))

ans = [[0 for _ in range(W)] for _ in range(H)]

idx = 1
for row in range(H):
    if '#' not in field[row]:
        continue

    conv = [1 if x == '#' else 0 for x in field[row]]
    cum = list(cumsum(conv))

    for i in range(W):
        if cum[i] == 0:
            cum[i] = 1

    for col in range(W):
        ans[row][col] = cum[col] + idx - 1

    idx += cum[-1]

for row in range(H):
    if ans[row][0] > 0:
        continue
    for r in range(row, H):
        if ans[r][0] > 0:
            ans[row] = ans[r]
            break

for row in range(H):
    if ans[row][0] > 0:
        continue
    for r in reversed(range(row)):
        if ans[r][0] > 0:
            ans[row] = ans[r]
            break

for row in ans:
    print(' '.join(map(str, row)))
