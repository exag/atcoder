"""
赤リンゴの上位X個、緑りんごの上位Y個を取ってきて、
それに無色りんごをあわせたもののうち、
上位X+Y個を取ってくるだけでよかった
"""
X, Y, A, B, C = map(int, input().split())

p = sorted(map(int, input().split()), reverse=True)[:X]
q = sorted(map(int, input().split()), reverse=True)[:Y]
r = list(map(int, input().split()))

apples = p + q + r
apples.sort(reverse=True)

print(sum(apples[: X + Y]))
