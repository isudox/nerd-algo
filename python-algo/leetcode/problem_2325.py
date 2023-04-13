"""2325. Decode the Message
https://leetcode.com/problems/decode-the-message/
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapper = {' ': ' '}
        i = 0
        for c in key:
            if c not in mapper:
                mapper[c] = chr(97 + i)
                i += 1
        ans = ''
        for c in message:
            ans += mapper[c]
        return ans
