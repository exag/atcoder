stdin = open('./sample.txt')
input = stdin.readline

# A, B, C = map(int, input().split())
# X, Y = map(int, input().split())
# L = sorted(map(int, input().split()))
# L = list(map(int, input().split()))
# A = [int(input()) for _ in range(3)]
# A = {int(input()) for _ in range(3)}
# N = int(input())
# S = input().strip()
# A, B = input().strip().split()
# L = input().strip().split()
# dp = [[0 for _ in range(W)] for _ in range(H)]
# --------------------

# pypy で書くと早くなるらしい
# import sys
# def input():
#     return sys.stdin.readline()[:-1]

N, A, B, C = map(int, input().split())

L = [int(input()) for _ in range(N)]



