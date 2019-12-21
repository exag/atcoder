"""
https://www.youtube.com/watch?v=tXsdcYBhmtI
"""

c = []
for i in range(3):
    c.append(list(map(int, input().split())))

x = [0] * 3
y = [0] * 3

for i in range(3):
    y[i] = c[0][i] - x[0]
for i in range(3):
    x[i] = c[i][0] - y[0]

for i in range(3):
    for j in range(3):
        if x[i] + y[j] != c[i][j]:
            print('No')
            exit()

print('Yes')
