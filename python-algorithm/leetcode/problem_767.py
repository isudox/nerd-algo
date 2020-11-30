"""767. Reorganize String
https://leetcode.com/problems/reorganize-string/

Given a string S, check if the letters can be rearranged so that
two characters that are adjacent to each other are not the same.

If possible, output any possible result.
If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""


class Solution:
    def reorganize_string(self, s: str) -> str:
        def greedy(ans: str) -> str:
            while len(ans) < len(s):
                for i in range(26):
                    if store[i]:
                        char = chr(ord('a') + i)
                        if not ans or char != ans[-1]:
                            ans = ans + char
                        elif char != ans[0]:
                            ans = char + ans
                        else:
                            flag = False
                            for j in range(1, len(ans)):
                                if ans[j] != char and ans[j - 1] != char:
                                    ans = ans[:j] + char + ans[j:]
                                    flag = True
                                    break
                            if not flag:
                                return ''
                        store[i] -= 1
            return ans

        store = [0] * 26
        for c in s:
            store[ord(c) - ord('a')] += 1
        return greedy('')

    def reorganize_string_2(self, s: str) -> str:
        def greedy(ans: str, cnt: int) -> str:
            while cnt < len(s):
                cur = ''
                for k in store.keys():
                    if store[k]:
                        cur += k
                        store[k] -= 1
                        cnt += 1
                if not ans or ans[-1] != cur[0]:
                    ans += cur
                elif ans[0] != cur[-1]:
                    ans = cur + ans
                else:
                    flag = False
                    for j in range(1, len(ans)):
                        if cur[0] != ans[j] and cur[0] != ans[j - 1]:
                            ans = ans[:j] + cur[0] + ans[j:]
                            flag = True
                            break
                    if not flag:
                        return ''
                    ans += cur[1:]
            return ans

        store = {}
        for c in s:
            store[c] = 1 + (store[c] if c in store else 0)
        return greedy('', 0)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reorganize_string_2("aab"))
    print(sol.reorganize_string_2("abccc"))
    print(sol.reorganize_string_2("aaabc"))
