"""514. Freedom Trail
https://leetcode.com/problems/freedom-trail/

Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.

Note:

    Length of both ring and key will be in range 1 to 100.
    There are only lowercase letters in both strings and might be some duplicate characters in both strings.
    It's guaranteed that string key could always be spelled by rotating the string ring.
"""
import sys
from typing import List


class Solution:
    def find_rotate_steps(self, ring: str, key: str) -> int:
        def min_rotate(from_idx: int, to_idx: int) -> int:
            diff = abs(from_idx - to_idx)
            return min(diff, ring_len - diff)

        def dfs(positions: List[int], ring_idx: int, key_idx: int) -> int:
            if memo[ring_idx][key_idx] != 0:
                return memo[ring_idx][key_idx]
            total_steps = sys.maxsize
            for pos in positions:
                cur_steps = min_rotate(ring_idx, pos) + 1
                if key_idx == key_len - 1:
                    total_steps = min(total_steps, cur_steps)
                    continue
                next_steps = dfs(char_idx[key[key_idx + 1]], pos, key_idx + 1)
                total_steps = min(total_steps, cur_steps + next_steps)
            memo[ring_idx][key_idx] = total_steps
            return total_steps

        key_len, ring_len = len(key), len(ring)
        char_idx = {}
        for i in range(ring_len):
            if ring[i] in char_idx:
                char_idx[ring[i]].append(i)
            else:
                char_idx[ring[i]] = [i]
        memo = [[0] * key_len for _ in range(ring_len)]
        return dfs(char_idx[key[0]], 0, 0)
