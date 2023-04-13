"""67. Add Binary
https://leetcode.com/problems/add-binary/
"""


def add_binary(a: str, b: str) -> str:
    len_a = len(a)
    len_b = len(b)
    n = min(len_a, len_b)
    pre = 0
    ans = ''
    for i in range(n):
        cur = int(a[len_a - i - 1]) + int(b[len_b - i - 1]) + pre
        x, y = divmod(cur, 2)
        ans = str(y) + ans
        pre = x
    c = a[:len_a - n] if len_a > n else b[:len_b - n]
    if pre == 0:
        return c + ans
    return add_binary(c, '1') + ans


def add_binary_1(a: str, b: str) -> str:
    m, n = len(a), len(b)
    if m < n:
        return add_binary_1(b, a)
    b = '0' * (m - n) + b
    ans = ''
    flag = 0
    for i in range(m - 1, -1, -1):
        x, y = int(a[i]), int(b[i])
        flag, z = divmod(x + y + flag, 2)
        ans = str(z) + ans
    return '1' + ans if flag else ans


def add_binary_2(a: str, b: str) -> str:
    """
    turn into decimal.
    """
    len_a = len(a)
    len_b = len(b)
    int_a, int_b = 0, 0
    for i in range(len_a):
        int_a += int(a[i]) * 2 ** (len_a - 1 - i)
    for i in range(len_b):
        int_b += int(b[i]) * 2 ** (len_b - 1 - i)
    int_sum = int_a + int_b
    if int_sum == 0:
        return '0'
    ans = ''
    while int_sum:
        int_sum, left = divmod(int_sum, 2)
        ans = str(left) + ans
    return ans
