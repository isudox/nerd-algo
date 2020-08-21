"""234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""
from common.list_node import ListNode


class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        """
        reverse a list
        time complexity: O(N)
        space complexity: O(N)
        """
        if not head:
            return True
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        return nums == nums[::-1]

    def is_palindrome_1(self, head: ListNode) -> bool:
        """
        reverse ListNode without creating extra space.
        time complexity: O(N)
        space complexity: O(1)
        """
        slow, fast = head, head
        left_half, right_half, prev = None, None, None
        while fast and fast.next:
            fast = fast.next.next
            temp = prev
            prev = slow
            slow = slow.next
            prev.next = temp
        left_half = prev
        right_half = slow.next if fast else slow
        while left_half and right_half:
            if left_half.val != right_half.val:
                return False
            left_half = left_half.next
            right_half = right_half.next
        return True
