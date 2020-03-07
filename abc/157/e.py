"""セグメント木

文字の種類の個数にはビット演算のORを使う
a -> 001
b -> 010
c -> 100
とすると、a | b | c = 111
となり、ビットが立っている個数が文字の種類になる
"""


class SegmentTree:
    def __init__(self, data):
        # 初期値
        self.default_value = 0
        # num: n以上の最小の2のべき乗
        self.power = 2 ** (N - 1).bit_length()
        self.node = [self.default_value] * 2 * self.power
        for i in range(N):
            self.node[i + self.power - 1] = 1 << (ord(data[i]) - 97)
        for i in range(self.power - 2, -1, -1):
            self.node[i] = self.node[2 * i + 1] | self.node[2 * i + 2]

    def update(self, k, x):
        k += self.power - 1
        self.node[k] = 1 << (ord(x) - 97)
        while k:
            k = (k - 1) // 2
            self.node[k] = self.node[k * 2 + 1] | self.node[k * 2 + 2]

    def query(self, left, right):
        if right <= left:
            return self.default_value
        left += self.power - 1
        right += self.power - 2
        ret = self.default_value
        while right - left > 1:
            if left & 1 == 0:
                ret = ret | self.node[left]
            if right & 1 == 1:
                ret = ret | self.node[right]
                right -= 1
            left = left // 2
            right = (right - 1) // 2
        if left == right:
            ret = ret | self.node[left]
        else:
            ret = (ret | self.node[left]) | self.node[right]
        return ret


N = int(input())
S = list(input().strip())
Q = int(input())
MAX_DIGIT = 26

st = SegmentTree(S)

for i in range(Q):
    q, a, b = map(str, input().split())
    if int(q) == 1:
        a = int(a) - 1
        st.update(a, b)
    if int(q) == 2:
        a = int(a) - 1
        b = int(b)
        res = st.query(a, b)
        ans = 0
        for d in range(MAX_DIGIT):
            if res >> d & 1:
                ans += 1
        print(ans)
