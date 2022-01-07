"""382. Linked List Random Node
https://leetcode.com/problems/linked-list-random-node/
"""
import random
from typing import Optional

from common.list_node import ListNode


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.store = []
        ptr = head
        while ptr:
            self.store.append(ptr.val)
            ptr = ptr.next
        self.n = len(self.store)

    def get_random(self) -> int:
        r = random.randrange(0, self.n)
        return self.store[r]
