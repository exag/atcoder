"""
Decimal を使うと高精度で小数の計算ができる
"""
from decimal import Decimal


a, b, c = map(int, input().split())

if Decimal(a).sqrt() + Decimal(b).sqrt() < Decimal(c).sqrt():
    print("Yes")
else:
    print("No")
