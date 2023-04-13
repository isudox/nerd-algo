"""917. Reverse Only Letters
https://leetcode.com/problems/reverse-only-letters/
"""


def reverse_only_letters(s: str) -> str:
    left, right = '', ''
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalpha():
            left += s[i]
            i += 1
            continue
        if not s[j].isalpha():
            right = s[j] + right
            j -= 1
            continue
        left += s[j]
        right = s[i] + right
        i += 1
        j -= 1
    if i == j:
        left += s[i]
    return left + right
