"""126. Word Ladder II
https://leetcode.com/problems/word-ladder-ii/

Given two words (beginWord and endWord), and a dictionary's word list,
find `all shortest` transformation sequence(s) from beginWord to endWord,
such that:

    Only one letter can be changed at a time
    Each transformed word must exist in the word list.
    Note that beginWord is not a transformed word.

Note:

    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
import string
from typing import List


class Solution:
    def find_ladders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        def next_words(word: str, word_set) -> List[str]:
            ret = []
            for i in range(len(word_set)):
                for c in list(string.ascii_lowercase):
                    tmp = word[:i] + c + word[i + 1:]
                    if tmp != word and tmp in word_set:
                        ret.append(tmp)
            return ret

        def bfs(word: str, word_set):
            queue = [word]
            dist = {word: 0}
            while queue:
                n = len(queue)
                for _ in range(n):
                    cur_word = queue.pop(0)
                    for next_word in next_words(cur_word, word_set):
                        if next_word not in dist:
                            dist[next_word] = dist[cur_word] + 1
                            queue.append(next_word)
            return dist

        def dfs(cur: str, target: str, word_set, distance, path: List[str], results):
            if cur == target:
                results.append(list(path))
                return
            for next_word in next_words(cur, word_set):
                if distance[next_word] != distance[cur] - 1:
                    continue
                path.append(next_word)
                dfs(next_word, target, word_set, distance, path, results)
                path.pop()

        word_set = set(word_list)
        if end_word not in word_set:
            return []
        word_set.add(begin_word)
        distance = bfs(end_word, word_set)
        ans = []
        dfs(begin_word, end_word, word_set, distance, [begin_word], ans)
        return ans
