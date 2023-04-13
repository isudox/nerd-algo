"""455. Assign Cookies
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie
that the child will be content with; and each cookie j has a size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i
will be content. Your goal is to maximize the number of your content children
and output the maximum number.

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

Constraints:

1 <= g.length <= 3 * 10^4
0 <= s.length <= 3 * 10^4
1 <= g[i], s[j] <= 2^31 - 1
"""
from typing import List
import bisect


class Solution:
    def find_content_children(self, g: List[int], s: List[int]) -> int:
        ans = 0
        g.sort()
        for i in s:
            idx = bisect.bisect(g, i)
            if idx > 0:
                ans += 1
                del g[idx - 1]
        return ans

    def find_content_children_2(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, m, n = 0, 0, len(g), len(s)
        ans = 0
        while i < m and j < n:
            if s[j] >= g[i]:
                ans += 1
                i += 1
            j += 1
        return ans
