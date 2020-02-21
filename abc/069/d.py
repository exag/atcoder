"""
色をキューに入れておいて、一筆書きしながら塗っていく
"""
H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

q = []
for i in range(N):
    q.extend([i+1] * A[i])

ans = [['' for _ in range(W)] for _ in range(H)]
for h in range(H):
    if h % 2 == 0:
        X = range(W)
    else:
        X = reversed(range(W))
    for w in X:
        ans[h][w] = str(q.pop())

for line in ans:
    print(' '.join(line))



