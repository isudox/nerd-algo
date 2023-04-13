class Solution:
    def num_decodings(self, s: str) -> int:
        def check1digit(c: str) -> int:
            if c == '0':
                return 0
            return 9 if c == '*' else 1

        def check2digits(a: str, b: str) -> int:
            if a == b == '*':
                return 15
            if a == '*':
                return 2 if b <= '6' else 1
            if b == '*':
                return 9 if a == '1' else (6 if a == '2' else 0)
            return int(a != '0' and int(a) * 10 + int(b) <= 26)

        mod = int(1e9 + 7)
        x, y, z = 0, 1, 0
        for i in range(1, len(s) + 1):
            z = y * check1digit(s[i - 1])
            if i > 1:
                z += x * check2digits(s[i - 2], s[i - 1])
            z %= mod
            x, y = y, z
        return z
