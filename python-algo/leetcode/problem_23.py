"""23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
"""
from typing import List, Optional
from common.list_node import ListNode
from heapq import heappush, heappop
import heapq
import collections


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i, node in enumerate(lists):
            if node:  # pq 为什么要传入三元组，这是因为 Python3 在 tuple[0] 相同的时候会继续比较后面的元素，而 ListNode 不具备比较关系，所以加一个 i 作为比较
                heappush(pq, (node.val, i, node))
        cur = dummy = ListNode(0)
        while pq:
            _, i, node = heappop(pq)
            if node.next:
                heappush(pq, (node.next.val, i, node.next))
            cur.next = node
            cur = cur.next
        return dummy.next


def merge_k_lists(lists: List[ListNode]) -> ListNode:
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
