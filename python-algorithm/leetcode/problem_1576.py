"""1576. Replace All ?'s to Avoid Consecutive Repeating Characters
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
"""


def modifyString(s: str) -> str:
    n = len(s)
    ans = ''
    for i in range(n):
        if s[i] != '?':
            ans += s[i]
            continue
        prev = ans[i - 1] if i > 0 else ''
        next = s[i + 1] if i < n - 1 else ''
        for x in range(97, 123):
            if chr(x) != prev and chr(x) != next:
                ans += chr(x)
                break
    return ans
