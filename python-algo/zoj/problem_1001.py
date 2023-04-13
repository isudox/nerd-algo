"""A + B Problem
https://zoj.pintia.cn/problem-sets/91827364500/problems/91827364500

Calculate a + b
"""
import sys

for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
