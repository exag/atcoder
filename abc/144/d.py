"""三角関数
場合分けの考え方
https://www.youtube.com/watch?v=JYLI4mZH-p8

math.atan2(底辺, 高さ) でラジアンが返ってくる
math.degrees(ラジアン) で角度が返ってくる
"""
import math

a, b, x = map(int, input().split())

s = x / a

if s >= a * b / 2:
    h = (a * b - s) * 2 / a
    radian = math.atan2(h, a)
else:
    w = s * 2 / b
    radian = math.atan2(b, w)
ans = math.degrees(radian)
print(ans)
