"""1418. Display Table of Food Orders in a Restaurant
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
"""
from typing import List
from collections import Counter


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        counters = [None] * 501
        foods = set()
        for order in orders:
            table = int(order[1])
            food = order[2]
            foods.add(food)
            if not counters[table]:
                counter = Counter()
                counter[food] += 1
                counters[table] = counter
            else:
                counters[table][food] += 1
            
        foods = list(foods)
        foods.sort()
        size = len(foods)
        pos_map = dict()
        for i, food in enumerate(foods):
            pos_map[food] = i
        ans = [['Table']]
        ans[0].extend(foods)
        for i in range(1, 501):
            if counters[i]:
                cur = [str(i)] + ['0'] * size
                for food, cnt in counters[i].items():
                    cur[pos_map[food] + 1] = str(cnt)
                ans.append(cur)
        return ans
        