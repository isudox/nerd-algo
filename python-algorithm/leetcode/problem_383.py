"""383. Ransom Note
https://leetcode.co/problems/ransom-note/
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        store = [0] * 26
        for ch in magazine:
            store[ord(ch) - 97] += 1
        for ch in ransomNote:
            store[ord(ch) - 97] -= 1
            if store[ord(ch) - 97] < 0:
                return False
        return True
