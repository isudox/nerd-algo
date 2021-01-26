"""1128. Number of Equivalent Domino Pairs
https://leetcode.com/problems/number-of-equivalent-domino-pairs/

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to
dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c)
that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length,
and dominoes[i] is equivalent to dominoes[j].

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Constraints:

    1 <= dominoes.length <= 40000
    1 <= dominoes[i][j] <= 9
For each domino j, find the number of dominoes you've already seen (dominoes i with i < j) that are equivalent
You can keep track of what you've seen using a hashmap
"""
from typing import List


class Solution:
    def num_equiv_domino_pairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        mapper = dict()
        for domino in dominoes:
            domino.sort()
            key = tuple(domino)
            if key in mapper:
                ans += mapper[key]
                mapper[key] += 1
            else:
                mapper[key] = 1
        return ans
