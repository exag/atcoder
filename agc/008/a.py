x, y = map(int, input().split())

ans = 10 ** 18
# 最初にB押す、最後にB押す
X, Y = -x, -y
if X <= Y:
    ans = min(ans, Y - X + 2)

# 最初にB押さない、最後にB押す
X, Y = x, -y
if X <= Y:
    ans = min(ans, Y - X + 1)

# 最初にB押す、最後にB押さない
X, Y = -x, y
if X <= Y:
    ans = min(ans, Y - X + 1)

# 最初にB押さない、最後にB押さない
X, Y = x, y
if X <= Y:
    ans = min(ans, Y - X)

print(ans)