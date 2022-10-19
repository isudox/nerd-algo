"""692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/

Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two
words have the same frequency, then the word with the lower alphabetical
order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
   Note that "i" comes before "love" due to a lower alphabetical order

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
   with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

Follow up:

Try to solve it in O(n log k) time and O(n) extra space.
"""
from typing import List
from collections import Counter
import heapq


class Solution:
    def top_k_frequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        mapper = [[] for _ in range(len(words) + 1)]
        for word, cnt in counter.items():
            mapper[cnt].append(word)
        ans = []
        for i in range(len(words), -1, -1):
            if len(ans) == k:
                return ans
            if mapper[i]:
                mapper[i].sort()
                if len(ans) + len(mapper[i]) <= k:
                    ans.extend(mapper[i])
                else:
                    ans.extend(mapper[i][:k - len(ans)])
        return ans

    def top_k_frequent2(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        pq = []  # store tuple of (cnt, word)
        for word, cnt in counter.items():
            if len(pq) < k:
                heapq.heappush(pq, Pair(cnt, word))
            elif pq[0].cnt < cnt or (pq[0].cnt == cnt and word < pq[0].word):
                heapq.heappop(pq)
                heapq.heappush(pq, Pair(cnt, word))
        ans = []
        while pq:
            ans.insert(0, heapq.heappop(pq).word)
        return ans


class Pair(object):
    def __init__(self, cnt: int, word: str):
        self.cnt = cnt
        self.word = word

    def __lt__(self, another):
        if self.cnt == another.cnt:
            return self.word > another.word
        return self.cnt < another.cnt
