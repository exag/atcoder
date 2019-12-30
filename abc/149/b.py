A, B, K = map(int, input().split())
A, K = A - min(A, K), K - min(A, K)
B -= min(B, K)
print(A, B)
