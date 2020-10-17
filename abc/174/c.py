"""
modKで考える
"""
# 解1
# K回繰り返して、Kの倍数がなかったらないとする
K = int(input())
x = 7 % K
for i in range(1, K+1):
    if x == 0:
        print(i)
        exit()
    x = (x * 10 + 7) % K
print(-1)

# 解2
# ループが起こるまで繰り返す
K = int(input())
x = 7 % K
s = set()
i = 1
while x not in s:
    if x == 0:
        print(i)
        exit()
    s.add(x)
    x = (x * 10 + 7) % K
    i += 1
print(-1)

