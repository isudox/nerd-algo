"""127. Word Ladder
https://leetcode.com/problems/word-ladder/

Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from typing import List


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    # BFS
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    word_len = len(end_word)
    queue = [begin_word]
    ans = 1
    while queue:
        n = len(queue)
        for i in range(n):
            cur_word = queue.pop(0)
            if cur_word == end_word:
                return ans
            for j in range(word_len):
                for k in range(26):
                    char = chr(ord('a') + k)
                    if char != cur_word[j]:
                        new_word = cur_word[:j] + char + cur_word[j + 1:]
                        if new_word in word_set:
                            word_set.remove(new_word)
                            queue.append(new_word)
        ans += 1
    return 0


def ladder_length_2(begin_word: str, end_word: str, word_list: List[str]) -> int:
    # Bi-BFS
    def bfs(q1: List[str], q2: List[str]) -> int:
        nonlocal ans
        while q1 and q2:
            n1, n2 = len(q1), len(q2)
            if n1 > n2:
                return bfs(q2, q1)
            for i in range(n1):
                cur_word = q1.pop(0)
                for j in range(word_len):
                    for k in range(26):
                        char = chr(ord('a') + k)
                        if char != cur_word[j]:
                            new_word = cur_word[:j] + char + cur_word[j + 1:]
                            if new_word in q2:
                                return ans + 1
                            if new_word in word_set:
                                word_set.remove(new_word)
                                q1.append(new_word)
            ans += 1
        return 0

    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    word_len = len(end_word)
    ans = 1
    return bfs([begin_word], [end_word])
