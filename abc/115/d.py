N, X = map(int, input().split())

a, p = [1], [1]
for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)


def f(N, X):
    if X == 1:
        return 0

    if X <= 1 + a[N-1]:
        return f(N-1, X-1)

    if X == 2 + a[N-1]:
        return p[N-1] + 1

    if X <= 2 + 2 * a[N-1]:
        return p[N-1] + 1 + f(N-1, X-2-a[N-1])

    if X == 3 + 2 * a[N-1]:
        return 2 * p[N-1] + 1


print(f(N, X))
