"""1093. Statistics from a Large Sample
https://leetcode.com/problems/statistics-from-a-large-sample/
"""
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mini = -1
        maxi = summ = mode = 0
        max_cnt = total_cnt = 0
        for i in range(len(count)):
            if count[i] > 0:
                summ += i * count[i]
                total_cnt += count[i]
                maxi = i
                if mini == -1:
                    mini = i
                if count[i] > max_cnt:
                    max_cnt = count[i]
                    mode = i
        flag = total_cnt % 2 == 1
        mid = (total_cnt + 1) // 2
        cnt = 0
        medians = []
        for i in range(len(count)):
            if len(medians) == 2:
                break
            if count[i] > 0 and mid <= cnt + count[i]:
                if flag:
                    medians = [i, i]
                    break
                medians.append(i)
                if len(medians) == 2:
                    break
                if cnt + count[i] > mid:
                    medians.append(i)
            cnt += count[i]
        return [mini, maxi, summ / total_cnt, sum(medians) / 2, mode]
