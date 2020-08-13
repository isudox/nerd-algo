"""212. Word Search II
https://leetcode.com/problems/word-search-ii/

Given a 2D board and a list of words from the dictionary,
find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""
from typing import List


class Solution:
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        def validate(w: str) -> bool:
            if w[0] not in pos:
                return False
            positions = pos[w[0]]
            for p in positions:
                memo = [[False] * cols for _ in range(rows)]
                if dfs(w, 1, p[0], p[1], memo):
                    return True
            return False

        def dfs(w: str, i: int, x: int, y: int, memo: List[List[bool]]) -> bool:
            if i == len(w):
                return True
            memo[x][y] = True
            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= x + d[0] < rows and 0 <= y + d[1] < cols and not \
                memo[x + d[0]][y + d[1]]:
                    if board[x + d[0]][y + d[1]] == w[i]:
                        memo[x + d[0]][y + d[1]] = True
                        if not dfs(w, i + 1, x + d[0], y + d[1], memo):
                            memo[x + d[0]][y + d[1]] = False
                        else:
                            return True
            return False

        if not board or not board[0]:
            return []

        pos = {}  # store the positions of char, {'a': [[0,1,], [0,2]]}
        rows, cols = len(board), len(board[0])
        for x in range(rows):
            for y in range(cols):
                if board[x][y] in pos:
                    pos[board[x][y]].append([x, y])
                else:
                    pos[board[x][y]] = [[x, y]]

        ans = []
        for word in words:
            if validate(word):
                ans.append(word)

        return ans


if __name__ == '__main__':
    sol = Solution()
    board = [["a", "b"], ["a", "a"]]
    words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]
    print(sol.find_words(board, words))
