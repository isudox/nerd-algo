"""726. Number of Atoms
https://leetcode.com/problems/number-of-atoms/
"""
import collections


class Solution:
    def count_of_atoms(self, formula: str) -> str:
        stack = list()
        i = 0
        while i < len(formula):
            c = formula[i]
            ordc = ord(c)
            if 65 <= ordc <= 90:
                stack.append([c, 1])  # 当前字符为大写，直接入栈
            elif 97 <= ordc <= 122:
                stack[-1][0] += c  # 当前字符为小写，取前一个字符，拼接
            elif 48 <= ordc <= 57:
                # 当前字符为数字
                num = c
                while i + 1 < len(formula) and 48 <= ord(formula[i + 1]) <= 57:
                    num += formula[i + 1]
                    i += 1
                if type(stack[-1]) == list:
                    stack[-1][1] *= int(num)
                else:
                    for k, v in stack[-1].items():
                        stack[-1][k] = v * int(num)
            elif c == '(':
                stack.append([c, 0])
            else:
                # 找到右括号，对左右括号内的元素进行合并
                merged_counter = collections.Counter()
                while stack and stack[-1][0] != '(':
                    last = stack.pop()
                    if type(last) == list:
                        merged_counter[last[0]] += last[1]
                    else:
                        for k, v in last.items():
                            merged_counter[k] += v
                stack.pop()
                # 再把合并后的结果回填到栈
                stack.append(merged_counter)
            i += 1
        counter = collections.Counter()
        while stack:
            last = stack.pop()
            if type(last) == list:
                counter[last[0]] += last[1]
            else:
                for k, v in last.items():
                    counter[k] += v
        char_list = list()
        for k in counter.keys():
            char_list.append(k)
        char_list.sort()
        ans = ''
        for char in char_list:
            ans += char + (str(counter[char]) if counter[char] > 1 else '')
        return ans
