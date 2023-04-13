"""394. Decode String
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside
the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

Constraints:

    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
"""


class Solution:
    def decode_string(self, s: str) -> str:
        char_stack, num_stack = [], []
        i, n = 0, len(s)
        while i < n:
            if s[i].isnumeric():
                cur = int(s[i])
                while i + 1 < n and s[i + 1].isnumeric():
                    i += 1
                    cur = cur * 10 + int(s[i])
                num_stack.append(cur)
            else:
                if s[i] == ']':
                    cur = ''
                    while char_stack:
                        if char_stack[-1].isalpha():
                            cur = char_stack.pop() + cur
                        elif char_stack[-1] == '[':
                            char_stack.pop()  # pop '['
                            char_stack.append(cur * num_stack.pop())
                            break
                else:
                    char_stack.append(s[i])
            i += 1
        return ''.join(char_stack)
