"""面试题 17.13. 恢复空格
https://leetcode-cn.com/problems/re-space-lcci/

哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
像句子"I reset the computer. It still didn't boot!"已经变成了"iresetthecomputeritstilldidntboot"。
在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数


示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。

提示：

0 <= len(sentence) <= 1000
dictionary中总字符数不超过 150000。
你可以认为dictionary和sentence中只包含小写字母。
"""
from typing import List


class Solution:
    def re_space(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i not in dictionary:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]
            for j in range(0, i):
                if sentence[j: i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
        return dp[n]
