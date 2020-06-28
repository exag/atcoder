

"""O(NlogN) 解法
約数をテーブルに保存していく
"""
N = int(input())
table = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        table[j] += 1
ans = 0
for i in range(N):
    i += 1
    ans += i * table[i]
print(ans)


""" O(N) 解法
https://www.youtube.com/watch?v=v8ppNGf49Nk&t=7059s
"""
def f(n):
    return n * (n+1) // 2

N = int(input())
ans = 0
for i in range(N):
    i += 1
    ans += i * f(N//i)
print(ans)
