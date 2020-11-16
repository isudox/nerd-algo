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
"""


class Solution:
    def decode_string(self, s: str) -> str:
        ans = ''
        k = 0
        stack = []
        cur_str = ''
        found_bracket = False
        for i in range(len(s)):
            if not found_bracket and s[i].isalpha():
                ans += s[i]
            elif found_bracket and s[i].isalpha():
                cur_str += s[i]
            elif s[i].isnumeric():
                k = k * 10 + int(s[i])
            elif s[i] == '[':
                found_bracket = True
            elif s[i] == ']':
                found_bracket = False
                ans += cur_str * k
                k = 0
                cur_str = ''
            else:
                cur_str += s[i]
        ans += cur_str
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.decode_string("3[a2[c]]"))  # "accaccacc"
