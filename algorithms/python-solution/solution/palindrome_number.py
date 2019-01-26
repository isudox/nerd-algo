# -*- coding: utf-8 -*-


class Solution(object):
    def is_palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return x >= 0 and str(x) == str(x)[::-1]
