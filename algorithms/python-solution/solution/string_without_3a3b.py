# -*- coding: utf-8 -*-


class Solution:
    def str_without_3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        res = ""
        while a and b:
            if a > b:
                res = res + "aab"
                a = a - 2
                b = b - 1
            elif a < b:
                res = res + "bba"
                a = a - 1
                b = b - 2
            else:
                res = res + "ab"
                a = a - 1
                b = b - 1
        if a:
            res = res + "a" * a
        if b:
            res = res + "b" * b
        return res
