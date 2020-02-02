"""
2017数を列挙して、累積和の配列を作っておく
"""
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


Q = int(input())
LR = []
for i in range(Q):
    l, r = map(int, input().split())
    LR.append((l, r))

c2017 = [0]
total = 0
for i in range(1, 10**5+1):
    if is_prime(i) and is_prime((i+1)//2):
        total += 1
    c2017.append(total)

for i in range(Q):
    l, r = LR[i]
    ans = (c2017[r] - c2017[l-1])
    print(ans)
