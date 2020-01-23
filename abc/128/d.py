"""
解説放送通り
https://www.youtube.com/watch?v=m-Nov1EvGoc
"""
N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for l in range(K+1):
    for r in range(K-l+1):
        if l + r > N:
            continue

        score = 0
        S = []

        for i in range(l):
            score += V[i]
            S.append(V[i])

        for i in range(r):
            score += V[-(i+1)]
            S.append(V[-(i+1)])

        d = K - l - r
        S.sort()
        for i in range(d):
            if i > len(S)-1:
                break
            if S[i] > 0:
                break
            score -= S[i]

        ans = max(ans, score)

print(ans)
