"""23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
⁠ 1->4->5,
⁠ 1->3->4,
⁠ 2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""
from typing import List
from common.list_node import ListNode
import heapq
import collections


class Solution:
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        ans = ListNode(0)
        mapper = collections.defaultdict(list)
        store = list()
        heapq.heapify(store)
        for node in lists:
            if node:
                heapq.heappush(store, node.val)
                mapper[node.val].append(node)
        p = ans
        while store:
            val = heapq.heappop(store)
            p.next = ListNode(val)
            p = p.next
            node = mapper[val].pop(0)
            if node.next:
                heapq.heappush(store, node.next.val)
                mapper[node.next.val].append(node.next)
        return ans.next
