"""909. Snakes and Ladders
https://leetcode.com/problems/snakes-and-ladders/description/
"""
import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def get_pos(pos: int) -> tuple:
            r, c = divmod((pos - 1), n)
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c

        n, sz = len(board), len(board) * len(board)
        q = collections.deque()
        q.append(1)
        visited = [False] * (n * n + 1)
        visited[1] = True
        ans = 0
        while q:
            m = len(q)
            ans += 1
            for _ in range(m):
                cur = q.popleft()
                for nxt in range(cur + 1, min(cur + 7, sz + 1)):
                    x, y = get_pos(nxt)
                    if board[x][y] > 0:
                        nxt = board[x][y]
                    if nxt == sz:
                        return ans
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
        return -1
