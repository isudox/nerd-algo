package com.leetcode;

/**
 * 19. Remove Nth Node From End of List
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 *
 * Given a linked list, remove the n-th node from the end of list and return
 * its head.
 *
 * Example:
 *
 * Given linked list: 1->2->3->4->5, and n = 2.
 *
 * After removing the second node from the end, the linked list becomes 1->2->3->5.
 * Note:
 *
 * Given n will always be valid.
 *
 * Follow up:
 *
 * Could you do this in one pass?
 */
public class RemoveNthNodeFromEndOfList {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode res = new ListNode(0);
        res.next = head;
        ListNode node1 = res, node2 = res;
        for (int i = 0; i < n; i++) node1 = node1.next;
        while (node1.next != null) {
            node1 = node1.next;
            node2 = node2.next;
        }
        node2.next = node2.next.next;
        return res.next;
    }
}
