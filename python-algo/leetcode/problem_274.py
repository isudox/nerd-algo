"""274. H-Index
https://leetcode.com/problems/h-index/"""
import collections
from typing import List


class Solution:
    def h_index(self, citations: List[int]) -> int:
        counter = collections.Counter()
        max_citation = 0
        for citation in citations:
            counter[citation] += 1
            max_citation = max(max_citation, citation)
        cnt = 0
        while max_citation:
            cnt += counter[max_citation]
            if cnt >= max_citation:
                return max_citation
            max_citation -= 1
        return 0

    def h_index_2(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for citation in citations:
            if citation > ans:
                ans += 1
        return ans
