"""382. Linked List Random Node
https://leetcode.com/problems/linked-list-random-node/
"""
import random
from typing import Optional

from common.list_node import ListNode


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def get_random(self) -> int:
        scope = 1
        chosen_val = 0
        cur = self.head
        while cur:
            if random.random() < 1 / scope:
                chosen_val = cur.val
            cur = cur.next
            scope += 1
        return chosen_val
