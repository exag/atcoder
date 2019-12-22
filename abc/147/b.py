S = input().strip()
R = S[::-1]

ans = 0
for s, r in zip(S, R):
    if s != r:
        ans += 1

print(ans//2)
