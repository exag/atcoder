"""
math.ceilは巨大な数字の場合は誤差が出るので、自分で用意する
"""
ceil = lambda a, b: -(-a // b)

K, A, B = map(int, input().split())
if A >= K:
    print(1)
    exit()
p = A - B
if p <= 0:
    print(-1)
    exit()

ans = 1
ans += ceil(K - A, A - B) * 2
print(ans)
