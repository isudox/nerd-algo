"""1178. Number of Valid Words for Each Puzzle
https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/description/

With respect to a given puzzle string, a word is valid if both the following
conditions are satisfied:

word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced",
"cabbage", and "baggage"; while invalid words are "beefed" (doesn't include
"a") and "based" (includes "s" which isn't in the puzzle).

Return an array answer, where answer[i] is the number of words in the given
word list words that are valid with respect to the puzzle puzzles[i].

Example :

Input:
words = ["aaaa","asas","able","ability","actt","actor","access"],
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa"
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There're no valid words for "gaswxyz" cause none of the words in the list
contains letter 'g'.

Constraints:

1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7
words[i][j], puzzles[i][j] are English lowercase letters.
Each puzzles[i] doesn't contain repeated characters.
"""
from typing import List


class Solution:
    def find_num_of_valid_words(self, words: List[str], puzzles: List[str]) -> List[int]:
        def cal(word: str) -> int:
            ret = 0
            for letter in word:
                ret += 1 << (ord(letter) - ord('a'))
            return ret

        n = len(puzzles)
        ans = [0] * n
        puzzle_nums = [0] * n
        for i in range(n):
            puzzle_nums[i] = cal(puzzles[i])
        for word in words:
            word_num = cal(''.join(set(word)))
            for i in range(n):
                if puzzles[i][0] in word and (word_num | puzzle_nums[i] == puzzle_nums[i]):
                    ans[i] += 1
        return ans
