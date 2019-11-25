# 2分探索
A, B, X = map(int, input().split())


def get_price(n):
    return A * n + B * len(str(n))


left = 0
right = 10 ** 9 + 1
while right - left > 1:
    mid = (left + right) // 2
    price = get_price(mid)
    if price <= X:
        left = mid
    if price > X:
        right = mid

print(left)
