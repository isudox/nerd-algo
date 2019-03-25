"""959. Regions Cut By Slashes
https://leetcode.com/problems/regions-cut-by-slashes/

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a
"/", "\", or blank space.
These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a "\" is represented as "\\".)

Return the number of regions.

Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""
from typing import List


class Solution:
    def regions_by_slashes(self, grid: List[str]) -> int:
        return 0
