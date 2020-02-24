"""自分の提出
"""
H, W, D = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

Q = int(input())
L = []
R = []
for i in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

M = dict()
for y, line in enumerate(A):
    for x, square in enumerate(line):
        M[square] = (x, y)

S = [[] for _ in range(D)]
for i in range(H * W):
    i += 1
    S[i % D].append(M[i])

CS = [[0] for _ in range(D)]
for i in range(D):
    for j in range(1, len(S[i])):
        CS[i].append(CS[i][j-1] + abs(S[i][j-1][0] - S[i][j][0]) + abs(S[i][j-1][1] - S[i][j][1]))

for i in range(Q):
    cumsum = CS[L[i] % D]
    left = (L[i]-1) // D
    right = (R[i]-1) // D
    print(cumsum[right] - cumsum[left])