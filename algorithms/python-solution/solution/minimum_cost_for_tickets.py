# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def min_cost_tickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        size = len(days)
        table = [[0, 0, 0] for _ in range(size + 1)]

        for i in range(1, size + 1):
            table[i][0] = costs[0] + min(table[i - 1])
            j = i
            while j > 0 and days[i - 1] - days[j - 1] < 7:
                j = j - 1
            table[i][1] = costs[1] + min(table[j])

            while j > 0 and days[i - 1] - days[j - 1] < 30:
                j = j - 1
            table[i][2] = costs[2] + min(table[j])

        return min(table[-1])
