from string import ascii_uppercase

uppers = ascii_uppercase + ascii_uppercase
N = int(input())
S = input().strip()

ans = ''
for s in S:
    idx = ascii_uppercase.find(s)
    ans += uppers[idx+N]
print(ans)
