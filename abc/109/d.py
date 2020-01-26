"""
解説放送通り
https://www.youtube.com/watch?v=zu0-rIh4ZXM

1行目〜最終-1行目
自分が奇数だったら、下のマスに1渡す
すると、奇数になりうるのは最終行だけになる

今度は最終行を左端からみていき、
自分が奇数だったら、右のマスに1渡す

こうすると、全体の和が偶数の時は全て偶数になり、
全体の和が奇数の時は右下1つのみが奇数になる
"""
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

cnt = 0
history = []

for h in range(H-1):
    for w in range(W):
        if A[h][w] == 0:
            continue
        if A[h][w] % 2 == 0:
            continue
        A[h][w] -= 1
        A[h+1][w] += 1
        cnt += 1
        history.append([h, w, h+1, w])

for w in range(W-1):
    if A[H-1][w] == 0:
        continue
    if A[H-1][w] % 2 == 0:
        continue
    A[H-1][w] -= 1
    A[H-1][w+1] += 1
    cnt += 1
    history.append([H-1, w, H-1, w+1])

print(cnt)
for fy, fx, ty, tx in history:
    print(fy+1, fx+1, ty+1, tx+1)
