Q, H, S, D = map(int, input().split())
N = int(input())

tea = [
    (Q, 0.25),
    (H, 0.5),
    (S, 1),
    (D, 2),
]
tea.sort(key=lambda x: x[0] / x[1])

ans = 0
remaining = N
for i in range(4):
    p, q = tea[i]
    # q が float なので d, m も float になり、後続の
    # ans += d * p で誤差が発生してしまうことがあるため int に直す
    d, m = map(int, divmod(remaining, q))
    if d == 0:
        continue
    ans += d * p
    remaining = m

print(int(ans))
