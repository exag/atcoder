"""
|x| = ±x なので、
max(|x| + |y| + |z|) は || を外して考えると、
max(
    max(+x + y + z),
    max(+x + y - z),
    max(+x - y + z),
    max(+x - y - z),
    max(-x + y + z),
    max(-x + y - z),
    max(-x - y + z),
    max(-x - y - z)
)
ということ
"""
n, m = map(int, input().split())
scores = [[] for _ in range(8)]
for i in range(n):
    x, y, z = map(int, input().split())
    scores[0].append(+x + y + z)
    scores[1].append(+x + y - z)
    scores[2].append(+x - y + z)
    scores[3].append(+x - y - z)
    scores[4].append(-x + y + z)
    scores[5].append(-x + y - z)
    scores[6].append(-x - y + z)
    scores[7].append(-x - y - z)

ans = 0
for i in range(8):
    scores[i].sort(reverse=True)
    ans = max(ans, sum(scores[i][:m]))

print(ans)
