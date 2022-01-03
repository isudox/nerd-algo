"""415. Add Strings
https://leetcode.com/problems/add-strings/
"""


def add_strings(num1: str, num2: str) -> str:
    l1, l2 = len(num1), len(num2)
    if l1 > l2:
        return add_strings(num2, num1)
    prev = 0
    tail = ''
    for i in range(l1):
        curr = int(num1[l1 - i - 1]) + int(num2[l2 - 1 - i]) + prev
        prev, curr = divmod(curr, 10)
        tail = str(curr) + tail
    if prev == 0:
        return num2[:l2 - l1] + tail
    if l1 == l2:
        return str(prev) + tail
    i, zeros = l2 - l1 - 1, ''
    while i >= 0 and num2[i] == '9':
        zeros += '0'
        i -= 1
    if i == -1:
        return '1' + zeros + tail
    return num2[:i] + str(int(num2[i]) + 1) + zeros + tail


def add_strings_2(num1: str, num2: str) -> str:
    l1, l2 = len(num1), len(num2)
    prev = 0
    ans = ''
    for i in range(max(l1, l2)):
        a = num1[l1 - 1 - i] if 0 <= l1 - 1 - i else '0'
        b = num2[l2 - 1 - i] if 0 <= l2 - 1 - i else '0'
        prev, curr = divmod((int(a) + int(b) + prev), 10)
        ans = str(curr) + ans
    return ('1' if prev else '') + ans


def add_strings_3(num1: str, num2: str) -> str:
    n, m = len(num1), len(num2)
    if n < m:
        return add_strings_3(num2, num1)
    num2 = '0' * (n - m) + num2
    prev = 0
    ans = ''
    for i in range(n - 1, -1, -1):
        prev, cur = divmod(int(num1[i]) + int(num2[i]) + prev, 10)
        ans = str(cur) + ans
    return ans if prev == 0 else '1' + ans
