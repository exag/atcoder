u"""
長さK以下の文字列だけ考えれば良い
"""

s = input().strip()
K = int(input())

S = set()
for i in range(len(s)):
    for w in range(1, K+1):
        S.add(s[i:i+w])

print(sorted(S)[K-1])

