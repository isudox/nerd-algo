"""537. Complex Number Multiplication
https://leetcode.com/problems/complex-number-multiplication/
"""


def complexNumberMultiply(num1: str, num2: str) -> str:
    x1, y1 = num1.split('+')
    x1 = int(x1)
    y1 = int(y1[:-1])
    x2, y2 = num2.split('+')
    x2 = int(x2)
    y2 = int(y2[:-1])
    x3 = x1 * x2 - y1 * y2
    y3 = x1 * y2 + x2 * y1
    return "{}+{}i".format(x3, y3)

