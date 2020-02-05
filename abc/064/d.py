"""
()をなくなるまで消していく
そうすると、
)))
(((
)))(((
のどれかになるはずなので、
足りないカッコを端に足す
"""
N = int(input())
S = input().strip()

replaced = S
while '()' in replaced:
    replaced = replaced.replace('()', '')

ans = ''
ans += '(' * list(replaced).count(')')
ans += S
ans += ')' * list(replaced).count('(')

print(ans)
