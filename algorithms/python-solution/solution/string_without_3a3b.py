# -*- coding: utf-8 -*-


class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ""
        while A and B:
            if A > B:
                res = res + "aab"
                A = A - 2
                B = B - 1
            elif A < B:
                res = res + "bba"
                A = A - 1
                B = B - 2
            else:
                res = res + "ab"
                A = A - 1
                B = B - 1
        if A:
            res = res + "a" * A
        if B:
            res = res + "b" * B
        return res
