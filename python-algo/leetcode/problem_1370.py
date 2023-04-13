"""1370. Increasing Decreasing String
https://leetcode.com/problems/increasing-decreasing-string/

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Constraints:

1 <= s.length <= 500
s contains only lower-case English letters.
从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
重复步骤 2 ，直到你没法从 s 中选择字符。
从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
重复步骤 5 ，直到你没法从 s 中选择字符。
重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
"""


class Solution:
    def sort_string(self, s: str) -> str:
        store = [0] * 26
        for c in s:
            store[ord(c) - ord('a')] += 1
        ans = ''
        count, n = 0, len(s)
        flag = True  # if pick minimum char
        while count < n:
            if flag:
                for i in range(26):
                    if store[i] > 0:
                        ans += chr(ord('a') + i)
                        store[i] -= 1
                        count += 1
            else:
                for i in range(25, -1, -1):
                    if store[i] > 0:
                        ans += chr(ord('a') + i)
                        store[i] -= 1
                        count += 1
            flag = not flag
        return ans
