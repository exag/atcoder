import string

S = string.ascii_lowercase
C = input().strip()
i = S.find(C)
print(S[i+1])

