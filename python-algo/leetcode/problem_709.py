"""709. To Lower Case
https://leetcode.com/problems/to-lower-case/
"""


def to_lower_case(s: str) -> str:
    ans = ''
    for ch in s:
        val = ord(ch)
        if 65 <= val <= 90:
            ans += chr(val + 32)
        else:
            ans += ch
    return ans
