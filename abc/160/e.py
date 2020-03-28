"""優先度付きキュー
"""
import heapq

X, Y, A, B, C = map(int, input().split())

p = sorted(map(int, input().split()), reverse=True)
q = sorted(map(int, input().split()), reverse=True)
r = sorted(map(int, input().split()), reverse=True)

red = p[:X]
green = q[:Y]
nocolor = r

heapq.heapify(red)
heapq.heapify(green)

for nc in nocolor:
    R = red[0]
    G = green[0]
    if R > nc and G > nc:
        break
    elif nc > R and nc > G:
        if R > G:
            q = heapq.heappop(green)
            heapq.heappush(green, nc)
        else:
            q = heapq.heappop(red)
            heapq.heappush(red, nc)
    elif nc > R:
        q = heapq.heappop(red)
        heapq.heappush(red, nc)
    elif nc > G:
        q = heapq.heappop(green)
        heapq.heappush(green, nc)

print(sum(red) + sum(green))
