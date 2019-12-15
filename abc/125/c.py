from itertools import accumulate
from fractions import gcd


N = int(input())
A = list(map(int, input().split()))

# 左からの累積GCD
cum_gcd_l = list(accumulate(A, gcd))
# 右からの累積GCD
cum_gcd_r = list(accumulate(reversed(A), gcd))[::-1]

ans = 0
for i in range(N):
    if i == 0:
        tmp = cum_gcd_r[1]
    elif i == N-1:
        tmp = cum_gcd_l[-2]
    else:
        tmp = gcd(cum_gcd_l[i-1], cum_gcd_r[i+1])
    ans = max(tmp, ans)

print(ans)

