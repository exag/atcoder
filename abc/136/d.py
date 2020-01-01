from math import ceil

S = input().strip()
L = len(S)
ans = [0] * L
for i in range(L):
    if S[i] == 'R' and S[i + 1] == 'L':
        ans[i] = 1
        ans[i+1] = 1
# Rだけ考える
cnt = 0
for i in range(L-1):
    if S[i] == 'R' and S[i+1] == 'L':
        ans[i] += cnt//2
        ans[i+1] += ceil(cnt/2)
        cnt = 0
    else:
        if S[i] == 'R':
            cnt += 1
# Lだけ考える
cnt = 0
for i in range(L-1):
    if S[-i-1] == 'L' and S[-i-2] == 'R':
        ans[-i-1] += cnt//2
        ans[-i-2] += ceil(cnt/2)
        cnt = 0
    else:
        if S[-i-1] == 'L':
            cnt += 1

print(' '.join([str(a) for a in ans]))

