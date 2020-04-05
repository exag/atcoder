k = int(input())

lunlun = [1,2,3,4,5,6,7,8,9]

p = 0

def generate_lunlun(p):
    last = p % 10
    if last - 1 >= 0:
        yield p * 10 + last - 1
    yield p * 10 + last
    if last + 1 <= 9:
        yield p * 10 + last + 1

while len(lunlun) < k:
    for new_lunlun in generate_lunlun(lunlun[p]):
        lunlun.append(new_lunlun)
    p += 1

print(lunlun[k-1])

