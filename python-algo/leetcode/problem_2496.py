"""2496. Maximum Value of a String in an Array
https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
"""


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        def helper(s: str) -> int:
            num = 0
            for c in s:
                if 97 <= ord(c) < 123:
                    return len(s)
                num = num * 10 + ord(c) - ord('0')
            return num

        ans = 0
        for s in strs:
            ans = max(ans, helper(s))
        return ans
