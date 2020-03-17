from string import ascii_uppercase


S = input().strip()
words = []
idx = 0
for i in range(1, len(S)):
    if S[i] in ascii_uppercase:
        if idx == i:
            continue
        words.append(S[idx:i+1])
        idx = i+1
words.sort(key=lambda x: x.upper())
print(''.join(words))