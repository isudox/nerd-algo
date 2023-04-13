"""491. Increasing Subsequences
https://leetcode.com/problems/increasing-subsequences/
"""
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        limit = 1 << n
        ans = []
        seen = set()
        for i in range(limit):
            sub, pre = [], -10000
            key = ''
            flag = True
            j = 0
            while i:
                ok = i & 1
                if ok:
                    if nums[j] < pre:
                        flag = False
                        break
                    sub.append(nums[j])
                    pre = nums[j]
                    key += '-' + str(nums[j])
                i >>= 1
                j += 1
            if flag and len(sub) > 1 and key not in seen:
                ans.append(sub)
                seen.add(key)
        return ans

    def find_subsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return []
        all_list, store = [], {}
        for i in range(n):
            new_append = []
            for ele in all_list:
                if ele[-1] <= nums[i]:
                    new_ele = ele[:]
                    new_ele.append(nums[i])
                    new_append.append(new_ele)
            if new_append:
                all_list.extend(new_append)
            if str(nums[i]) not in store:
                all_list.append([nums[i]])
                store[str(nums[i])] = True
        ans = []
        for ele in all_list:
            if len(ele) > 1:
                key = ','.join(map(str, ele))
                if key not in store:
                    ans.append(ele)
                    store[key] = True

        return ans
