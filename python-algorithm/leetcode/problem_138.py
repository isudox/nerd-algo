"""138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer
points to, or null if it does not point to any node.
"""


class Solution:

    def copy_random_list(self, head: 'Node') -> 'Node':
        if not head:
            return head
        store, index = {}, {}
        p = head
        i = 0
        while p:
            store[i] = Node(x=p.val)
            index[p] = i
            p = p.next
            i += 1
        p = head
        for j in range(i):
            if j < i - 1:
                store.get(j).next = store.get(j + 1)
            if p.random:
                store.get(j).random = store.get(index.get(p.random))
            p = p.next
        return store[0]

    def copy_random_list_2(self, head: 'Node') -> 'Node':
        """
        for-loop 2 times.
        time complexity: O(N)
        space complexity: O(N)
        """
        if not head:
            return head
        store = {}
        p = head
        while p:
            store[p] = Node(x=p.val)
            p = p.next
        p = head
        while p:
            if p.next:
                store.get(p).next = store.get(p.next)
            if p.random:
                store.get(p).random = store.get(p.random)
            p = p.next
        return store[head]

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
