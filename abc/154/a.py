S, T = input().strip().split()
A, B = map(int, input().split())
U = input().strip()

if S == U:
    A -= 1
else:
    B -= 1

print(A, B)
